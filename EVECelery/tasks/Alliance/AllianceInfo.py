from EVECelery.tasks.BaseTasks.TaskESI import TaskESI


class AllianceInfo(TaskESI):
    def default_ttl(self) -> int:
        return 3600  # current esi x-cached-seconds header

    def route(self, alliance_id: int):
        return f"/alliances/{alliance_id}"
