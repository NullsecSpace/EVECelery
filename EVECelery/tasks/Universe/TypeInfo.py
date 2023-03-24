from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError


class TypeInfo(ESIRequest):
    def route(self, type_id: int):
        return f"/universe/types/{type_id}"

    def validate_inputs(self, type_id: int) -> None:
        try:
            int(type_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")

