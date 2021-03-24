import asyncio
import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

import pytest
from rich import inspect, print

from eve_esi_jobs.job_to_action import make_action_from_job
from eve_esi_jobs.models import deserialize_json_job
from eve_esi_jobs.pfmsoft.util.async_actions.aiohttp import (
    AiohttpAction,
    AiohttpQueueWorker,
    do_aiohttp_action_queue,
)

LOG_LEVEL = logging.INFO


@pytest.fixture(scope="module")
def logger(test_log_path):
    log_file_name = f"{__name__}.log"
    _logger = logging.getLogger(__name__)
    if not os.path.exists(test_log_path):
        os.mkdir(test_log_path)
    file_handler = RotatingFileHandler(
        test_log_path / Path(log_file_name), maxBytes=102400, backupCount=10
    )
    format_string = "%(asctime)s %(levelname)s:%(funcName)s: %(message)s [in %(pathname)s:%(lineno)d]"
    file_handler.setFormatter(logging.Formatter(format_string))
    file_handler.setLevel(LOG_LEVEL)
    _logger.addHandler(file_handler)
    _logger.setLevel(LOG_LEVEL)
    ############################################################
    # NOTE add file handler to other library modules as needed #
    ############################################################
    # async_logger = logging.getLogger("eve_esi_jobs")
    # async_logger.addHandler(file_handler)
    return _logger


def test_save_job_to_file(esi_provider, test_app_dir):

    file_path: Path = test_app_dir / Path("data/test.json")
    esi_job_json = {
        "op_id": "get_markets_region_id_history",
        "retry_limit": 1,
        "parameters": {"region_id": 10000002, "type_id": 34},
        "result_callbacks": {
            "success": [
                {"callback_id": "response_to_json"},
                {
                    "callback_id": "save_json_to_file",
                    "kwargs": {"file_path": file_path},
                },
            ]
        },
    }
    esi_job = deserialize_json_job(esi_job_json)
    action = make_action_from_job(esi_job, esi_provider)
    worker = AiohttpQueueWorker()
    asyncio.run(do_aiohttp_action_queue([action], [worker]))
    assert action.result is not None
    assert len(action.result) > 5
    keys = ["average", "date", "highest", "lowest", "order_count", "volume"]
    assert all(key in keys for key in action.result[0])
    assert action.context["esi_job"]["op_id"] == "get_markets_region_id_history"
    assert file_path.exists()
    assert file_path.stat().st_size > 10