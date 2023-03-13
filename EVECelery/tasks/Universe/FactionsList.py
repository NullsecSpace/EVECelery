from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest


class FactionsList(ESIRequest):
    def get_key(self):
        return f"FactionsList"

    def route(self):
        return f"/universe/factions"

    def validate_inputs(self, **kwargs) -> None:
        return

