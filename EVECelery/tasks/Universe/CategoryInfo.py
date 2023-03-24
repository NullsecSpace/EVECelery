from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest
from EVECelery.exceptions.tasks import InputValidationError


class CategoryInfo(ESIRequest):
    def route(self, category_id: int):
        return f"/universe/categories/{category_id}"

    def validate_inputs(self, category_id: int) -> None:
        try:
            int(category_id)
        except ValueError:
            raise InputValidationError("Input parameter must be an integer.")

