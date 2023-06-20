from tests.TestUtils import *
from EVECelery import TaskDirectory
from EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_icons import Response200_get_alliances_alliance_id_icons


class Test_get_alliances_alliance_id_icons:
    t = TaskDirectory.ESI.Alliance.get_alliances_alliance_id_icons

    def test_get_sync(self, mock_env_celery):
        assert self.t.cache_key_exists(alliance_id=1727758877) is False
        r = self.t.get_sync(alliance_id=1727758877, kwargs_get={'timeout': 5})
        assert isinstance(r, Response200_get_alliances_alliance_id_icons)
        assert r.body.px128x128 == 'https://images.evetech.net/Alliance/1727758877_128.png'
        assert r.body.px64x64 == 'https://images.evetech.net/Alliance/1727758877_64.png'

