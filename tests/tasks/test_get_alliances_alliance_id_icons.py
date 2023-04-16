from tests.TestUtils import *
from EVECelery.tasks import TasksESI
from EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_icons import ResponseSuccess200_get_alliances_alliance_id_icons


class Test_get_alliances_alliance_id_icons:
    t = TasksESI.Alliance.get_alliances_alliance_id_icons

    def test_get_sync(self, mock_env_celery):
        assert self.t.cache_key_exists(alliance_id=1727758877) is False
        r = self.t.get_sync(alliance_id=1727758877, kwargs_get={'timeout': 5})
        assert isinstance(r, ResponseSuccess200_get_alliances_alliance_id_icons)
        assert r.px128x128 == 'https://images.evetech.net/Alliance/1727758877_128.png'
        assert r.px64x64 == 'https://images.evetech.net/Alliance/1727758877_64.png'

