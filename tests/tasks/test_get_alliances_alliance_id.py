from tests.TestUtils import *
from EVECelery import TaskDirectory
from EVECelery.tasks.ESI.Alliance.get_alliances_alliance_id import Response200_get_alliances_alliance_id
from pydantic import ValidationError
from EVECelery.exceptions.tasks import CachedException


class Test_get_alliances_alliance_id:
    t = TaskDirectory.ESI.Alliance.get_alliances_alliance_id

    def test_get_sync(self, mock_env_celery):
        assert self.t.cache_key_exists(alliance_id=1727758877) is False
        r = self.t.get_sync(alliance_id=1727758877, kwargs_get={'timeout': 5})
        assert isinstance(r, Response200_get_alliances_alliance_id)
        assert r.body.ticker == 'NC'
        assert r.body.name == 'Northern Coalition.'
        assert r.cache.hit is False
        assert self.t.cache_key_exists(alliance_id=1727758877, datasource='tranquility') is True

        # new call
        r2 = self.t.get_sync(alliance_id=1727758877, datasource='tranquility', kwargs_get={'timeout': 5})
        assert r2.cache.hit is True

    def test_get_sync_bad_args(self):
        """
        validation of args to task before calling ESI
        """
        with pytest.raises(ValidationError):
            self.t.get_sync(alliance_id='badid')

    def test_get_sync_cached_exception(self, mock_env_celery):
        """
        call endpoint with correctly formatted argument but an invalid ESI ID
        """
        bad_id = 10000000000
        assert self.t.cache_key_exists(alliance_id=bad_id, datasource='tranquility') is False
        with pytest.raises(CachedException) as e:
            self.t.get_sync(alliance_id=10000000000)
        assert '400' in str(e.value)
        assert self.t.cache_key_exists(alliance_id=bad_id, datasource='tranquility') is True
        with pytest.raises(CachedException) as e:
            self.t.get_sync(alliance_id=10000000000)
        assert '400' in str(e.value)
