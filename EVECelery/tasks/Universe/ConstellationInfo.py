from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError
from .RegionInfo import RegionInfo


class ConstellationInfo(ESIRequest):
    def get_key(self, constellation_id: int):
        return f"ConstellationInfo-{constellation_id}"

    def route(self, constellation_id: int):
        return f"/universe/constellations/{constellation_id}"

    def _hook_after_esi_success(self, esi_response: dict) -> None:
        region_id = esi_response.get("region_id")
        if region_id:
            RegionInfo().get_async(ignore_result=True, region_id=region_id)

    def validate_inputs(self, constellation_id: int) -> None:
        try:
            int(constellation_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


