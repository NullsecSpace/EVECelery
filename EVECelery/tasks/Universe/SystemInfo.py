from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError


class SystemInfo(ESIRequest):
    def route(self, system_id: int):
        return f"/universe/systems/{system_id}"

    def validate_inputs(self, system_id: int) -> None:
        try:
            int(system_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


