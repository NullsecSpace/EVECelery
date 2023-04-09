from EVECelery.tasks.BaseTasks.ESIResqust import ESIRequest


class CharacterPublicInfo(ESIRequest):
    def default_ttl(self) -> int:
        return 86400  # current esi x-cached-seconds header

    def route(self, character_id: int):
        return f"/characters/{character_id}"
