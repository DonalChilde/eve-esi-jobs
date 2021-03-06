import logging

from eve_esi_jobs import models
from eve_esi_jobs.examples.jobs import get_markets_region_id_history

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def example_workorder():

    region_id = 10000002
    type_id = 34
    work_order = models.EsiWorkOrder(
        name="example_workorder",
        output_path="samples/workorder_output/${ewo_name}",
        description=(
            "An example of a workorder, with a collection of "
            "jobs whose output is gathered under a file path defined in the workorder."
        ),
    )
    callbacks = []
    callbacks.append(
        models.JobCallback(
            callback_id="save_result_to_json_file",
            kwargs={
                "file_path_template": "${esi_job_id_}/market-history-${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    callbacks.append(
        models.JobCallback(
            callback_id="save_result_to_yaml_file",
            kwargs={
                "file_path_template": "${esi_job_id_}/market-history-${region_id}-${type_id}-esi-job.yaml"
            },
        )
    )
    job = get_markets_region_id_history(region_id, type_id, callbacks)
    job.name = "Save market history as json"
    job.id_ = 1
    job.description = (
        "Get the market history for Tritainium in The Forge "
        "region, and save it to a json file."
    )

    work_order.jobs.append(job)
    #####
    callbacks = []
    callbacks.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path_template": "${esi_job_id_}/market-history-${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    callbacks.append(
        models.JobCallback(
            callback_id="save_result_to_json_file",
            kwargs={
                "file_path_template": "${esi_job_id_}/market-history-${region_id}-${type_id}.json"
            },
        )
    )
    job_2 = get_markets_region_id_history(region_id, type_id, callbacks)
    job_2.name = "Save market history and job as json"
    job_2.id_ = 2
    job_2.description = (
        "Get the market history for Tritainium in The Forge "
        "region, and save it to a json file. Also save the job, "
        "including the response metadata, to a separate json file."
    )

    work_order.jobs.append(job_2)
    #####
    callbacks = []
    callbacks.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path_template": "${esi_job_id_}/market-history-${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    callbacks.append(
        models.JobCallback(
            callback_id="save_list_of_dict_result_to_csv_file",
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
                "file_path_template": "${esi_job_id_}/market-history-${region_id}-${type_id}.csv",
            },
        )
    )
    job_3 = get_markets_region_id_history(region_id, type_id, callbacks)
    job_3.name = "Save market history as csv and job with data as json"
    job_3.id_ = 3
    job_3.description = (
        "Get the market history for Tritainium in The Forge "
        "region, and save it to a csv file. The region_id and type_id added to each row, "
        "and the columns are given a custom order. "
        "Also save the job, including the response metadata and the result data, "
        "to a separate json file."
    )

    work_order.jobs.append(job_3)
    #####
    callbacks = []
    callbacks.append(
        models.JobCallback(
            callback_id="save_result_to_json_file",
            kwargs={
                "file_path_template": "${esi_job_id_}/public-contracts/${region_id}.json"
            },
        )
    )
    job_4 = models.EsiJob(
        name="get paged data",
        description="Get the all the pages from a paged api.",
        id_=4,
        op_id="get_contracts_public_region_id",
        parameters={"region_id": 10000002},
        callbacks=callbacks,
    )

    work_order.jobs.append(job_4)
    return work_order


def response_to_job_json_file():
    work_order = models.EsiWorkOrder(
        name="response_to_job_json_file",
        output_path="samples/order_output/${ewo_name}",
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
    job.callbacks.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path_template": "data/market-history/${region_id}-${type_id}-esi-job.json"
            },
        )
    )

    return work_order


def result_to_job_json_file():
    work_order = models.EsiWorkOrder(
        name="result_to_job_json_file",
        output_path="samples/order_output/${ewo_name}",
        description=(
            "An example of saving a completed job to a json file, with result data"
        ),
    )
    job = models.EsiJob(
        op_id="get_markets_region_id_history",
        parameters={"region_id": 10000002, "type_id": 34},
    )
    work_order.jobs.append(job)
    job.callbacks.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path_template": "data/market-history/${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    return work_order


def result_to_json_file_and_response_to_json_file():
    work_order = models.EsiWorkOrder(
        name="result_to_json_file_and_response_to_json_file",
        output_path="samples/order_output/${ewo_name}",
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
    job.callbacks.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path_template": "data/market-history/${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    job.callbacks.append(
        models.JobCallback(
            callback_id="save_result_to_json_file",
            kwargs={
                "file_path_template": "data/market-history/${region_id}-${type_id}.json"
            },
        )
    )
    return work_order


def result_and_response_to_job_json_file():
    work_order = models.EsiWorkOrder(
        name="result_and_response_to_job_json_file",
        output_path="samples/order_output/${ewo_name}",
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
    job.callbacks.append(
        models.JobCallback(
            callback_id="save_esi_job_to_json_file",
            kwargs={
                "file_path_template": "data/market-history/${region_id}-${type_id}-esi-job.json"
            },
        )
    )
    return work_order


def result_to_json_file():
    work_order = models.EsiWorkOrder(
        name="result_to_json_file",
        output_path="samples/order_output/${ewo_name}",
        description=("An example of saving the raw results to a json file."),
    )
    job = models.EsiJob(
        op_id="get_markets_region_id_history",
        parameters={"region_id": 10000002, "type_id": 34},
    )
    work_order.jobs.append(job)
    job.callbacks.append(
        models.JobCallback(
            callback_id="save_result_to_json_file",
            kwargs={
                "file_path_template": "data/market-history/${region_id}-${type_id}.json"
            },
        )
    )
    return work_order


def result_to_csv_file():
    work_order = models.EsiWorkOrder(
        name="result_to_csv_file",
        output_path="samples/order_output/${ewo_name}",
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
    job.callbacks.append(
        models.JobCallback(
            callback_id="save_list_of_dict_result_to_csv_file",
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
                "file_path_template": "data/market-history/${region_id}-${type_id}.csv",
            },
        )
    )
    return work_order


def result_with_pages_to_json_file():
    work_order = models.EsiWorkOrder(
        name="result_with_pages_to_json_file",
        output_path="samples/order_output/${ewo_name}",
        description=(
            "An example of saving the raw results with a paged api to a json file."
        ),
    )
    job = models.EsiJob(
        op_id="get_contracts_public_region_id",
        parameters={"region_id": 10000002},
    )
    work_order.jobs.append(job)
    job.callbacks.append(
        models.JobCallback(
            callback_id="save_result_to_json_file",
            kwargs={"file_path_template": "data/public-contracts/${region_id}.json"},
        )
    )
    return work_order
