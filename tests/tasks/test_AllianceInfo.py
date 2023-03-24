from tests.TestUtils import *
from EVECelery.tasks.Alliance import *


class TestAllianceInfo:
    def test_get_sync(self, mock_env_celery):
        assert AllianceInfo().cache_key_exists(alliance_id=1727758877) is False
        r = AllianceInfo().get_sync(timeout=5, alliance_id=1727758877)
        assert isinstance(r, dict)
        assert r['ticker'] == 'NC'
        assert r['name'] == 'Northern Coalition.'
        assert AllianceInfo().cache_key_exists(alliance_id=1727758877) is True
