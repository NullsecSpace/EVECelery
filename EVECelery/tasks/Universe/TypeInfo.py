from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest


class TypeInfo(ESIRequest):
    def route(self, type_id: int):
        return f"/universe/types/{type_id}"
