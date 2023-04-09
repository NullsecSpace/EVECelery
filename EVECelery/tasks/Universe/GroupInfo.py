from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest

class GroupInfo(ESIRequest):
    def route(self, group_id: int):
        return f"/universe/groups/{group_id}"
