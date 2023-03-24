from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest


class FactionsList(ESIRequest):
    def route(self):
        return f"/universe/factions"

    def validate_inputs(self, **kwargs) -> None:
        return

