from celery import Task
import redis


class BaseTask(Task):
    _redis: redis.Redis = None
    _redis_user: str = None
    _redis_host: str = None
    _redis_port: int = None
    _redis_db: int = None
    _redis_password: str = None

    @property
    def redis(self) -> redis.Redis:
        if self._redis is None:
            self._redis = redis.Redis(username=self._redis_user, host=self._redis_host, port=self._redis_port,
                                      db=self._redis_db, password=self._redis_password)
        return self._redis

    @classmethod
    def set_redis_details(cls, host, port, db, user, password):
        cls._redis_host = host
        cls._redis_port = port
        cls._redis_db = db
        cls._redis_user = user
        cls._redis_password = password

