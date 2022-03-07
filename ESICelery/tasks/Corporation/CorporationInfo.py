from ESICelery.tasks.BaseTasks.ESIResqust import ESIRequest
from ESICelery.exceptions.tasks import InputValidationError


class CorporationInfo(ESIRequest):
    def ttl_404(self) -> int:
        return 3600  # current esi x-cached-seconds header

    def get_key(self, corporation_id: int):
        return f"CorporationInfo-{corporation_id}"

    def route(self, corporation_id: int):
        return f"/corporations/{corporation_id}"

    def validate_inputs(self, corporation_id: int) -> None:
        try:
            int(corporation_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


