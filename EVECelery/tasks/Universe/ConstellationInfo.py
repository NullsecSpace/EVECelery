from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError


class ConstellationInfo(ESIRequest):
    def route(self, constellation_id: int):
        return f"/universe/constellations/{constellation_id}"

    def validate_inputs(self, constellation_id: int) -> None:
        try:
            int(constellation_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


