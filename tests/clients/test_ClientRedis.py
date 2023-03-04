from tests.TestUtils import *
import pytest
from ESICelery.clients.ClientRedis import *
from pydantic import ValidationError
from redis.exceptions import ConnectionError, AuthenticationError


class TestClientRedis:
    def test_init_params(self):
        """
        provide params and ensure model has correct values
        """
        c = ClientRedis(user='testuser', password='testpass', host='localhost', port=1000, db=0)
        assert c.config.user == 'testuser'
        assert c.config.password == 'testpass'
        assert c.config.host == 'localhost'
        assert c.config.port == 1000
        assert c.config.db == 0

    def test_init_raises_invalid_db(self):
        """
        provide an invalid db number that doesn't exist in redis
        """
        with pytest.raises(ValidationError):
            c = ClientRedis(user='testuser', password='testpass', host='localhost', port=1000, db=16)
        with pytest.raises(ValidationError):
            c = ClientRedis(user='testuser', password='testpass', host='localhost', port=1000, db=-1)

    def test_check_connection_active_db(self, server_redis):
        """
        should connect and return True
        """
        c = ClientRedis(user=server_redis['user'], password=server_redis['pass'], host=server_redis['host'],
                        port=server_redis['port'], db=1)
        assert c.check_connection() is True

    def test_check_connection_invalid_password(self, server_redis):
        """
        should connect and return auth error
        """
        c = ClientRedis(user=server_redis['user'], password='badpass', host=server_redis['host'],
                        port=server_redis['port'], db=1)
        with pytest.raises(AuthenticationError):
            c.check_connection()

    def test_check_connection_no_db(self):
        """
        Should raise exec when testing connection to a redis db that is not started
        """
        c = ClientRedis(user='testuser', password='testpass', host='localhost', port=1000, db=1)
        with pytest.raises(ConnectionError):
            c.check_connection()


class TestClientRedisResultBackend:
    def test_init_raises_on_no_input(self):
        """
        provide no input or env vars to redis client should cause system exit
        """
        with pytest.raises(SystemExit):
            c = ClientRedisResultBackend()

    def test_envar_init_single_redis_node(self, mock_env_redis):
        """
        os vars set explicitly for a single redis node install
        """
        c = ClientRedisResultBackend()
        assert c.config.user == mock_env_redis.get('EVECelery_Redis_ResultBackend_User')
        assert c.config.password == mock_env_redis.get('EVECelery_Redis_ResultBackend_Password')
        assert c.config.host == mock_env_redis.get('EVECelery_Redis_ResultBackend_Host')
        assert c.config.port == mock_env_redis.get('EVECelery_Redis_ResultBackend_Port')
        assert c.config.db == mock_env_redis.get('EVECelery_Redis_ResultBackend_DB')

        assert c.check_connection() is True


class TestClientRedisLocks:
    def test_init_raises_on_no_input(self):
        """
        provide no input or env vars to redis client should cause system exit
        """
        with pytest.raises(SystemExit):
            c = ClientRedisLocks()

    def test_envar_init_multi_redis_node(self, monkeypatch):
        """
        os vars set explicitly for a multiple redis nodes install
        """
        env_vars = {
            'EVECelery_Redis_Locks_User': 'user2',
            'EVECelery_Redis_Locks_Password': 'pass2',
            'EVECelery_Redis_Locks_Host': 'localhost',
            'EVECelery_Redis_Locks_Port': 6380,
            'EVECelery_Redis_Locks_DB': 5
        }
        for k, v in env_vars.items():
            monkeypatch.setenv(k, v)

        c = ClientRedisLocks()
        assert c.config.user == env_vars['EVECelery_Redis_Locks_User']
        assert c.config.password == env_vars['EVECelery_Redis_Locks_Password']
        assert c.config.host == env_vars['EVECelery_Redis_Locks_Host']
        assert c.config.port == env_vars['EVECelery_Redis_Locks_Port']
        assert c.config.db == env_vars['EVECelery_Redis_Locks_DB']

    def test_envar_init_single_redis_node(self, mock_env_redis):
        """
        os vars set explicitly for a single redis node install
        """
        c = ClientRedisLocks()
        assert c.config.user == mock_env_redis.get('EVECelery_Redis_ResultBackend_User')
        assert c.config.password == mock_env_redis.get('EVECelery_Redis_ResultBackend_Password')
        assert c.config.host == mock_env_redis.get('EVECelery_Redis_ResultBackend_Host')
        assert c.config.port == mock_env_redis.get('EVECelery_Redis_ResultBackend_Port')
        assert c.config.db == mock_env_redis.get('EVECelery_Redis_ResultBackend_DB') + 1

        assert c.check_connection() is True


class TestClientRedisCache:
    def test_init_raises_on_no_input(self):
        """
        provide no input or env vars to redis client should cause system exit
        """
        with pytest.raises(SystemExit):
            c = ClientRedisCache()

    def test_envar_init_multi_redis_node(self, monkeypatch):
        """
        os vars set explicitly for a multiple redis nodes install
        """
        env_vars = {
            'EVECelery_Redis_Cache_User': 'user2',
            'EVECelery_Redis_Cache_Password': 'pass2',
            'EVECelery_Redis_Cache_Host': 'localhost',
            'EVECelery_Redis_Cache_Port': 6380,
            'EVECelery_Redis_Cache_DB': 5
        }
        for k, v in env_vars.items():
            monkeypatch.setenv(k, v)

        c = ClientRedisCache()
        assert c.config.user == env_vars['EVECelery_Redis_Cache_User']
        assert c.config.password == env_vars['EVECelery_Redis_Cache_Password']
        assert c.config.host == env_vars['EVECelery_Redis_Cache_Host']
        assert c.config.port == env_vars['EVECelery_Redis_Cache_Port']
        assert c.config.db == env_vars['EVECelery_Redis_Cache_DB']

    def test_envar_init_single_redis_node(self, mock_env_redis):
        """
        os vars set explicitly for a single redis node install
        """
        c = ClientRedisCache()
        assert c.config.user == mock_env_redis.get('EVECelery_Redis_ResultBackend_User')
        assert c.config.password == mock_env_redis.get('EVECelery_Redis_ResultBackend_Password')
        assert c.config.host == mock_env_redis.get('EVECelery_Redis_ResultBackend_Host')
        assert c.config.port == mock_env_redis.get('EVECelery_Redis_ResultBackend_Port')
        assert c.config.db == mock_env_redis.get('EVECelery_Redis_ResultBackend_DB') + 2

        assert c.check_connection() is True
