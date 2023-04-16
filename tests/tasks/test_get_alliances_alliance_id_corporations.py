from tests.TestUtils import *
from EVECelery.tasks import TasksESI
from EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id_corporations import ResponseSuccess200_get_alliances_alliance_id_corporations


class Test_get_alliances_alliance_id_corporations:
    t = TasksESI.Alliance.get_alliances_alliance_id_corporations

    def test_get_sync(self, mock_env_celery):
        r = self.t.get_sync(alliance_id=1727758877, kwargs_get={'timeout': 5})  # show corps for NC.
        assert isinstance(r, ResponseSuccess200_get_alliances_alliance_id_corporations)
        assert isinstance(r.items, list)
        assert 935907718 in r.items  # assert Dice is in NC.
        assert 1727573569 in r.items  # executor corp in alliance
