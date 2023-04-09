from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest

class RegionInfo(ESIRequest):
    def route(self, region_id: int):
        return f"/universe/regions/{region_id}"
