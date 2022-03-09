from celery import Task
import redis
import ESICelery.config


class BaseTask(Task):
    _redis: redis.Redis = None

    def __init__(self):
        self.name = self.__class__.__name__

    @property
    def redis(self) -> redis.Redis:
        if self._redis is None:
            self._redis = redis.Redis(username=ESICelery.config.redis_user,
                                      host=ESICelery.config.redis_host,
                                      port=ESICelery.config.redis_port,
                                      db=ESICelery.config.redis_db,
                                      password=ESICelery.config.redis_password)
        return self._redis
