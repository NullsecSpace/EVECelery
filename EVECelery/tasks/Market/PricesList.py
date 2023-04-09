from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest


class PricesList(ESIRequest):
    def route(self):
        return f"/markets/prices"
