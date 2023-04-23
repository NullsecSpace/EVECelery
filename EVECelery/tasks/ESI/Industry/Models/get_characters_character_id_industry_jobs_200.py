"""
A model definition module returned by an ESI task.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/ESI_Models.py'.
"""
from __future__ import annotations
from EVECelery.tasks.BaseTasks.Models.ModelsBase import ModelBaseEVECelery
from EVECelery.tasks.BaseTasks.Models.ModelsCached import ModelCachedResponse
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class GetCharactersCharacterIdIndustryJobsOkItem(BaseModel):
    activity_id: int = Field(
        ...,
        description='Job activity ID',
        title='get_characters_character_id_industry_jobs_activity_id',
    )
    blueprint_id: int = Field(
        ...,
        description='blueprint_id integer',
        title='get_characters_character_id_industry_jobs_blueprint_id',
    )
    blueprint_location_id: int = Field(
        ...,
        description='Location ID of the location from which the blueprint was installed. Normally a station ID, but can also be an asset (e.g. container) or corporation facility',
        title='get_characters_character_id_industry_jobs_blueprint_location_id',
    )
    blueprint_type_id: int = Field(
        ...,
        description='blueprint_type_id integer',
        title='get_characters_character_id_industry_jobs_blueprint_type_id',
    )
    completed_character_id: Optional[int] = Field(
        None,
        description='ID of the character which completed this job',
        title='get_characters_character_id_industry_jobs_completed_character_id',
    )
    completed_date: Optional[datetime] = Field(
        None,
        description='Date and time when this job was completed',
        title='get_characters_character_id_industry_jobs_completed_date',
    )
    cost: Optional[float] = Field(
        None,
        description='The sume of job installation fee and industry facility tax',
        title='get_characters_character_id_industry_jobs_cost',
    )
    duration: int = Field(
        ...,
        description='Job duration in seconds',
        title='get_characters_character_id_industry_jobs_duration',
    )
    end_date: datetime = Field(
        ...,
        description='Date and time when this job finished',
        title='get_characters_character_id_industry_jobs_end_date',
    )
    facility_id: int = Field(
        ...,
        description='ID of the facility where this job is running',
        title='get_characters_character_id_industry_jobs_facility_id',
    )
    installer_id: int = Field(
        ...,
        description='ID of the character which installed this job',
        title='get_characters_character_id_industry_jobs_installer_id',
    )
    job_id: int = Field(
        ...,
        description='Unique job ID',
        title='get_characters_character_id_industry_jobs_job_id',
    )
    licensed_runs: Optional[int] = Field(
        None,
        description='Number of runs blueprint is licensed for',
        title='get_characters_character_id_industry_jobs_licensed_runs',
    )
    output_location_id: int = Field(
        ...,
        description='Location ID of the location to which the output of the job will be delivered. Normally a station ID, but can also be a corporation facility',
        title='get_characters_character_id_industry_jobs_output_location_id',
    )
    pause_date: Optional[datetime] = Field(
        None,
        description='Date and time when this job was paused (i.e. time when the facility where this job was installed went offline)',
        title='get_characters_character_id_industry_jobs_pause_date',
    )
    probability: Optional[float] = Field(
        None,
        description='Chance of success for invention',
        title='get_characters_character_id_industry_jobs_probability',
    )
    product_type_id: Optional[int] = Field(
        None,
        description='Type ID of product (manufactured, copied or invented)',
        title='get_characters_character_id_industry_jobs_product_type_id',
    )
    runs: int = Field(
        ...,
        description='Number of runs for a manufacturing job, or number of copies to make for a blueprint copy',
        title='get_characters_character_id_industry_jobs_runs',
    )
    start_date: datetime = Field(
        ...,
        description='Date and time when this job started',
        title='get_characters_character_id_industry_jobs_start_date',
    )
    station_id: int = Field(
        ...,
        description='ID of the station where industry facility is located',
        title='get_characters_character_id_industry_jobs_station_id',
    )
    status: Literal[
        'active', 'cancelled', 'delivered', 'paused', 'ready', 'reverted'
    ] = Field(
        ...,
        description='status string',
        title='get_characters_character_id_industry_jobs_status',
    )
    successful_runs: Optional[int] = Field(
        None,
        description='Number of successful runs for this job. Equal to runs unless this is an invention job',
        title='get_characters_character_id_industry_jobs_successful_runs',
    )


class GetCharactersCharacterIdIndustryJobsOk(BaseModel):
    __root__: List[GetCharactersCharacterIdIndustryJobsOkItem] = Field(
        ...,
        description='200 ok array',
        max_items=2000,
        title='get_characters_character_id_industry_jobs_ok',
    )


class Headers200_get_characters_character_id_industry_jobs(ModelBaseEVECelery):
    """
    Headers for response code 200
    """

    Cache_Control: str | None = Field(
        description="The caching mechanism used", alias="Cache-Control"
    )
    ETag: str | None = Field(description="RFC7232 compliant entity tag")
    Expires: str | None = Field(description="RFC7231 formatted datetime string")
    Last_Modified: str | None = Field(
        description="RFC7231 formatted datetime string", alias="Last-Modified"
    )


class Response200_get_characters_character_id_industry_jobs(ModelCachedResponse):
    """
    Industry jobs placed by a character

    Response for code 200. This model contains the response body and headers returned from ESI.

    Example responses from ESI:

    .. code-block:: json

        [
          {
            "activity_id": 1,
            "blueprint_id": 1015116533326,
            "blueprint_location_id": 60006382,
            "blueprint_type_id": 2047,
            "cost": 118.01,
            "duration": 548,
            "end_date": "2014-07-19T15:56:14Z",
            "facility_id": 60006382,
            "installer_id": 498338451,
            "job_id": 229136101,
            "licensed_runs": 200,
            "output_location_id": 60006382,
            "runs": 1,
            "start_date": "2014-07-19T15:47:06Z",
            "station_id": 60006382,
            "status": "active"
          }
        ]

    """

    headers: Headers200_get_characters_character_id_industry_jobs = Field(
        ..., description='The response headers for this request.'
    )
    body: GetCharactersCharacterIdIndustryJobsOk = Field(
        ..., description='The response body for this request.'
    )
