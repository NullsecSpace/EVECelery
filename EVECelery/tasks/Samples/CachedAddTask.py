from EVECelery.tasks.BaseTasks.TaskCached import TaskCached
from EVECelery.exceptions.tasks import CachedException
from EVECelery.tasks.BaseTasks.TaskCached import ModelCachedSuccess, ModelCachedException


class ModelResponse(ModelCachedSuccess):
    result: float


class AddTask(TaskCached):
    def _run_get_result(self, a, b):
        try:
            return ModelResponse(result=a + b)
        except Exception as ex:
            return ModelCachedException(exception_message=str(ex), cache_ttl=60)
