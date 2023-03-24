from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError


class AllianceInfo(ESIRequest):
    def ttl_404(self) -> int:
        return 3600  # current esi x-cached-seconds header

    def route(self, alliance_id: int):
        return f"/alliances/{alliance_id}"

    def validate_inputs(self, alliance_id: int) -> None:
        try:
            int(alliance_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")

