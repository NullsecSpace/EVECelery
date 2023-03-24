from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError


class GroupInfo(ESIRequest):
    def route(self, group_id: int):
        return f"/universe/groups/{group_id}"

    def validate_inputs(self, group_id: int) -> None:
        try:
            int(group_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


