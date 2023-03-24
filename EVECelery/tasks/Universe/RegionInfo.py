from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError


class RegionInfo(ESIRequest):
    def route(self, region_id: int):
        return f"/universe/regions/{region_id}"

    def validate_inputs(self, region_id: int) -> None:
        try:
            int(region_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


