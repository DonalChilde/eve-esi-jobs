import logging

from eve_esi_jobs import models

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def response_to_job_json_file():
    work_order = models.EsiWorkOrder(
        name="response_to_job_json_file",
        parent_path_template="samples/order_output/${ewo_name}",
        description=(
            "An example of saving a completed job to a json file,"
            " including the response data. Result data intentionaly left out."
        ),
    )
    job = models.EsiJob(
        op_id="get_markets_region_id_history",
        parameters={"region_id": 10000002, "type_id": 34},
    )
    work_order.jobs.append(job)
    job.callbacks.success.append(
        models.JobCallback(callback_id="response_content_to_json")
    )
    job.callbacks.success.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.success.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path": "data/market-history/${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    job.callbacks.fail.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.fail.append(models.JobCallback(callback_id="log_job_failure"))
    return work_order


def result_to_job_json_file():
    work_order = models.EsiWorkOrder(
        name="result_to_job_json_file",
        parent_path_template="samples/order_output/${ewo_name}",
        description=(
            "An example of saving a completed job to a json file, with result data"
        ),
    )
    job = models.EsiJob(
        op_id="get_markets_region_id_history",
        parameters={"region_id": 10000002, "type_id": 34},
    )
    work_order.jobs.append(job)
    job.callbacks.success.append(
        models.JobCallback(callback_id="response_content_to_json")
    )
    job.callbacks.success.append(models.JobCallback(callback_id="result_to_esi_job"))
    job.callbacks.success.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path": "data/market-history/${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    job.callbacks.fail.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.fail.append(models.JobCallback(callback_id="log_job_failure"))
    return work_order


def result_to_json_file_and_response_to_json_file():
    work_order = models.EsiWorkOrder(
        name="result_to_json_file_and_response_to_json_file",
        parent_path_template="samples/order_output/${ewo_name}",
        description=(
            "An example of saving the raw results to a json file,"
            " and the job with response data to a separate json file"
        ),
    )
    job = models.EsiJob(
        op_id="get_markets_region_id_history",
        parameters={"region_id": 10000002, "type_id": 34},
    )
    work_order.jobs.append(job)
    job.callbacks.success.append(
        models.JobCallback(callback_id="response_content_to_json")
    )
    job.callbacks.success.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.success.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path": "data/market-history/${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    job.callbacks.success.append(
        models.JobCallback(
            callback_id="save_json_result_to_file",
            kwargs={"file_path": "data/market-history/${region_id}-${type_id}.json"},
        )
    )
    job.callbacks.fail.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.fail.append(models.JobCallback(callback_id="log_job_failure"))
    return work_order


def result_and_response_to_job_json_file():
    work_order = models.EsiWorkOrder(
        name="result_and_response_to_job_json_file",
        parent_path_template="samples/order_output/${ewo_name}",
        description=(
            "An example of saving a completed job to a json file,"
            " with result and response data"
        ),
    )
    job = models.EsiJob(
        op_id="get_markets_region_id_history",
        parameters={"region_id": 10000002, "type_id": 34},
    )
    work_order.jobs.append(job)
    job.callbacks.success.append(
        models.JobCallback(callback_id="response_content_to_json")
    )
    job.callbacks.success.append(models.JobCallback(callback_id="result_to_esi_job"))
    job.callbacks.success.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.success.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path": "data/market-history/${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    job.callbacks.fail.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.fail.append(models.JobCallback(callback_id="log_job_failure"))
    return work_order


def result_to_json_file():
    work_order = models.EsiWorkOrder(
        name="result_to_json_file",
        parent_path_template="samples/order_output/${ewo_name}",
        description=("An example of saving the raw results to a json file."),
    )
    job = models.EsiJob(
        op_id="get_markets_region_id_history",
        parameters={"region_id": 10000002, "type_id": 34},
    )
    work_order.jobs.append(job)
    job.callbacks.success.append(
        models.JobCallback(callback_id="response_content_to_json")
    )

    job.callbacks.success.append(
        models.JobCallback(
            callback_id="save_json_result_to_file",
            kwargs={"file_path": "data/market-history/${region_id}-${type_id}.json"},
        )
    )
    job.callbacks.fail.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.fail.append(models.JobCallback(callback_id="log_job_failure"))
    return work_order


def result_to_csv_file():
    work_order = models.EsiWorkOrder(
        name="result_to_csv_file",
        parent_path_template="samples/order_output/${ewo_name}",
        description=(
            "An example of saving the json results to a csv file. Also, shows "
            "reordering columns, and adding additional columns"
        ),
    )
    job = models.EsiJob(
        op_id="get_markets_region_id_history",
        parameters={"region_id": 10000002, "type_id": 34},
    )
    work_order.jobs.append(job)
    job.callbacks.success.append(
        models.JobCallback(callback_id="response_content_to_json")
    )

    job.callbacks.success.append(
        models.JobCallback(
            callback_id="save_list_of_dict_result_to_csv_file",
            config={
                "file_path_template": "data/market-history/${region_id}-${type_id}.csv"
            },
            kwargs={
                "additional_fields": {"region_id": 10000002, "type_id": 34},
                "field_names": [
                    "date",
                    "average",
                    "highest",
                    "lowest",
                    "order_count",
                    "volume",
                    "region_id",
                    "type_id",
                ],
            },
        )
    )
    job.callbacks.fail.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.fail.append(models.JobCallback(callback_id="log_job_failure"))
    return work_order


def result_with_pages_to_json_file():
    work_order = models.EsiWorkOrder(
        name="result_with_pages_to_json_file",
        parent_path_template="samples/order_output/${ewo_name}",
        description=(
            "An example of saving the raw results with a paged api to a json file."
        ),
    )
    job = models.EsiJob(
        op_id="get_contracts_public_region_id",
        parameters={"region_id": 10000002},
    )
    work_order.jobs.append(job)
    job.callbacks.success.append(
        models.JobCallback(callback_id="response_content_to_json")
    )
    job.callbacks.success.append(models.JobCallback(callback_id="check_for_pages"))
    job.callbacks.success.append(
        models.JobCallback(
            callback_id="save_json_result_to_file",
            kwargs={"file_path": "data/public-contracts/${region_id}.json"},
        )
    )
    job.callbacks.fail.append(models.JobCallback(callback_id="response_to_esi_job"))
    job.callbacks.fail.append(models.JobCallback(callback_id="log_job_failure"))
    return work_order