from tests.TestUtils import *
from EVECelery import TaskDirectory
from EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_corporations import Response200_get_alliances_alliance_id_corporations


class Test_get_alliances_alliance_id_corporations:
    t = TaskDirectory.ESI.Alliance.get_alliances_alliance_id_corporations

    def test_get_sync(self, mock_env_celery):
        r = self.t.get_sync(alliance_id=1727758877, kwargs_get={'timeout': 5})  # show corps for NC.
        assert isinstance(r, Response200_get_alliances_alliance_id_corporations)
        r = r.dict()
        assert isinstance(r['body'], list)
        assert 935907718 in r['body']  # assert Dice is in NC.
        assert 1727573569 in r['body']  # executor corp in alliance
