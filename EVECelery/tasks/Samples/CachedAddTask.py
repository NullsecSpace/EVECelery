from EVECelery.tasks.BaseTasks.CachedTask import CachedTask


class CachedAddTask(CachedTask):
    def _run_get_result(self, a, b):
        return a + b, 5
