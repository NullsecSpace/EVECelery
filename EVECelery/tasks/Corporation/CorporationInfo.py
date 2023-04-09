from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError


class CorporationInfo(ESIRequest):
    def default_ttl(self) -> int:
        return 3600  # current esi x-cached-seconds header

    def route(self, corporation_id: int):
        return f"/corporations/{corporation_id}"

    def validate_inputs(self, corporation_id: int) -> None:
        try:
            int(corporation_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


