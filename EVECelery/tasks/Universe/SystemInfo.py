from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError
from .ConstellationInfo import ConstellationInfo


class SystemInfo(ESIRequest):
    def get_key(self, system_id: int):
        return f"SystemInfo-{system_id}"

    def route(self, system_id: int):
        return f"/universe/systems/{system_id}"

    def _hook_after_esi_success(self, esi_response: dict) -> None:
        constellation_id = esi_response.get("constellation_id")
        if constellation_id:
            ConstellationInfo().get_async(ignore_result=True, constellation_id=constellation_id)

    def validate_inputs(self, system_id: int) -> None:
        try:
            int(system_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


