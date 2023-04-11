from tests.TestUtils import *
from EVECelery.tasks.BaseTasks.TaskCached import TaskCached


class TestCacheTask:
    def test_get_redis_locks_success(self, mock_env_redis):
        r = TaskCached().redis_locks
        assert r.ping() is True
        assert r.get_connection_kwargs()['db'] == 1

    def test_get_redis_cache_success(self, mock_env_redis):
        r = TaskCached().redis_cache
        assert r.ping() is True
        assert r.get_connection_kwargs()['db'] == 1

    def test_get_redis_locks_fail(self):
        with pytest.raises(SystemExit):
            r = TaskCached().redis_locks

    def test_get_redis_cache_fail(self):
        with pytest.raises(SystemExit):
            r = TaskCached().redis_cache
