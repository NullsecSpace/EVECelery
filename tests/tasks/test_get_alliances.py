from tests.TestUtils import *
from EVECelery import TaskDirectory
from EVECelery.tasks.ESI.Alliance.get_alliances import Response200_get_alliances


class Test_get_alliances:
    t = TaskDirectory.ESI.Alliance.get_alliances

    def test_get_sync(self, mock_env_celery):
        r = self.t.get_sync(kwargs_get={'timeout': 5})
        assert isinstance(r, Response200_get_alliances)
        r = r.dict()
        assert isinstance(r['body'], list)
        assert len(r['body']) > 500
        assert 1727758877 in r['body']  # assert NC. alliance id exists in dataset
