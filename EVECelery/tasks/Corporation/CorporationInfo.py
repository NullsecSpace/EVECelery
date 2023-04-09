from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest


class CorporationInfo(ESIRequest):
    def default_ttl(self) -> int:
        return 3600  # current esi x-cached-seconds header

    def route(self, corporation_id: int):
        return f"/corporations/{corporation_id}"
