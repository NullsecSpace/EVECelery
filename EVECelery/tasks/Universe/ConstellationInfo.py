from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest

class ConstellationInfo(ESIRequest):
    def route(self, constellation_id: int):
        return f"/universe/constellations/{constellation_id}"
