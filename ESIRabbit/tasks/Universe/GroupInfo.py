from ESIRabbit.tasks.BaseTasks.ESIResqust import ESIRequest
from ESIRabbit.exceptions.tasks import InputValidationError
from .CategoryInfo import CategoryInfo


class GroupInfo(ESIRequest):
    def get_key(self, group_id: int):
        return f"GroupInfo-{group_id}"

    def route(self, group_id: int):
        return f"/universe/groups/{group_id}"

    def _hook_after_esi_success(self, esi_response: dict) -> None:
        category_id = esi_response.get("category_id")
        if category_id:
            CategoryInfo().get_async(ignore_result=True, category_id=category_id)

    def validate_inputs(self, group_id: int) -> None:
        try:
            int(group_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")


