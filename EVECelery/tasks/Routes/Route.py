from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest


class Route(ESIRequest):
    def route(self, origin: int, destination: int):
        return f"/route/{origin}/{destination}"
