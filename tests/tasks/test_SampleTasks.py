from tests.TestUtils import *
from EVECelery.tasks.Samples import *


class TestSampleAdd:
    def test_get_sync(self, mock_env_celery):
        assert CachedAddTask().cache_key_exists(a=5, b=5) is False
        assert CachedAddTask().get_sync(a=5, b=5, kwargs_get={'timeout': 5}) == 10
        assert CachedAddTask().cache_key_exists(a=5, b=5) is True

