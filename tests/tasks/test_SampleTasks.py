from tests.TestUtils import *
from EVECelery.tasks.Samples import *


class TestSampleAdd:
    def test_get_sync(self, mock_env_celery):
        assert CachedAddTask().cache_key_exists(a=5, b=5) is False
        assert CachedAddTask().get_sync(timeout=5, a=5, b=5) == 10
        assert CachedAddTask().cache_key_exists(a=5, b=5) is True

    def test_get_async(self, mock_env_celery):
        assert CachedAddTask().cache_key_exists(a=10, b=5) is False
        r = CachedAddTask().get_async(a=10, b=5)
        assert r.get(timeout=1) == 15
        assert CachedAddTask().cache_key_exists(a=10, b=5) is True
