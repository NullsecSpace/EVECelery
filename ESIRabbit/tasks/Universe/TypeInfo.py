from ESIRabbit.tasks.BaseTasks.ESIResqust import ESIRequest
from ESIRabbit.exceptions.tasks import InputValidationError
from .GroupInfo import GroupInfo


class TypeInfo(ESIRequest):
    def get_key(self, type_id: int):
        return f"TypeInfo-{type_id}"

    def route(self, type_id: int):
        return f"/universe/types/{type_id}"

    def _hook_after_esi_success(self, esi_response: dict) -> None:
        group_id = esi_response.get("group_id")
        if group_id:
            GroupInfo().get_async(ignore_result=True, group_id=group_id)

    def validate_inputs(self, type_id: int) -> None:
        try:
            int(type_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")

