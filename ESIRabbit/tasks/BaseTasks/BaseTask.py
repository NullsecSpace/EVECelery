from celery import Task
import redis
import ESIRabbit.config


class BaseTask(Task):
    _redis: redis.Redis = None

    @property
    def redis(self) -> redis.Redis:
        if self._redis is None:
            self._redis = redis.Redis(username=ESIRabbit.config.redis_user,
                                      host=ESIRabbit.config.redis_host,
                                      port=ESIRabbit.config.redis_port,
                                      db=ESIRabbit.config.redis_db,
                                      password=ESIRabbit.config.redis_password)
        return self._redis
