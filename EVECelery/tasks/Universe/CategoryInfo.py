from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest

class CategoryInfo(ESIRequest):
    def route(self, category_id: int):
        return f"/universe/categories/{category_id}"
