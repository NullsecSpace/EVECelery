from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest


class PricesList(ESIRequest):
    def get_key(self):
        return f"PricesList"

    def route(self):
        return f"/markets/prices"

    def validate_inputs(self, **kwargs) -> None:
        return


