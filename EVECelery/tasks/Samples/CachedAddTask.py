from EVECelery.tasks.BaseTasks.CachedTask import CachedTask
from EVECelery.exceptions.tasks import CachedException
from EVECelery.tasks.BaseTasks.CachedTask import ModelCachedSuccess, ModelCachedException


class ModelResponse(ModelCachedSuccess):
    result: float


class CachedAddTask(CachedTask):
    def _run_get_result(self, a, b):
        try:
            return ModelResponse(result=a + b)
        except Exception as ex:
            return ModelCachedException(exception_message=str(ex), cache_ttl=60)
