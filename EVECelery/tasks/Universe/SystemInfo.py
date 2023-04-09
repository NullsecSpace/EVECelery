from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest

class SystemInfo(ESIRequest):
    def route(self, system_id: int):
        return f"/universe/systems/{system_id}"
