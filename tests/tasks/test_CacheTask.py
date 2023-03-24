from tests.TestUtils import *
from EVECelery.tasks.BaseTasks.CachedTask import CachedTask


class TestCacheTask:
    def test_get_redis_locks_success(self, mock_env_redis):
        r = CachedTask().redis_locks
        assert r.ping() is True
        assert r.get_connection_kwargs()['db'] == 2

    def test_get_redis_cache_success(self, mock_env_redis):
        r = CachedTask().redis_cache
        assert r.ping() is True
        assert r.get_connection_kwargs()['db'] == 3

    def test_get_redis_locks_fail(self):
        with pytest.raises(SystemExit):
            r = CachedTask().redis_locks

    def test_get_redis_cache_fail(self):
        with pytest.raises(SystemExit):
            r = CachedTask().redis_cache
