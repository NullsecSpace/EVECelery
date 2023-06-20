from tests.TestUtils import *
from EVECelery.tasks.Samples.CachedAddTask import *


class TestSampleAdd:
    def test_get_sync(self, mock_env_celery):
        assert AddTask().cache_key_exists(a=5, b=5) is False
        r = AddTask().get_sync(a=5, b=5, kwargs_get={'timeout': 5})
        assert isinstance(r, ModelResponse) is True
        assert r.cache.hit is False
        assert r.result == 10
        assert AddTask().cache_key_exists(a=5, b=5) is True

        assert AddTask().get_sync(a=5, b=5, kwargs_get={'timeout': 5}).cache.hit is True
