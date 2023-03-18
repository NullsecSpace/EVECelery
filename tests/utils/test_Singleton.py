from tests.TestUtils import *
import pytest
from EVECelery.utils.Singleton import Singleton


class TestSingleton:
    def test_ref_same_singleton(self, mock_env_no_servers):
        """
        test that two different classes refer to the same singleton
        """

        from EVECelery.clients.ClientRedis import ClientRedisLocks
        from EVECelery.clients.ClientRabbitMQ import ClientRabbitMQ

        assert len(Singleton._instances) == 0

        rabbitmq = ClientRabbitMQ()
        assert len(Singleton._instances) == 1
        assert 'ClientRabbitMQ' in Singleton._instances

        reddislock = ClientRedisLocks()
        assert len(Singleton._instances) == 2
        assert 'ClientRedisLocks' in Singleton._instances

    def test_different_import_names(self, mock_env_no_servers):
        """
        test that two different classes refer to the same singleton
        """

        from EVECelery.clients.ClientRedis import ClientRedisLocks
        from EVECelery.clients import ClientRedis as ClientRedisLocksRenamed
        from EVECelery.clients.ClientRedis import ClientRedisLocks as ClientRedisLocksRenamed2

        assert len(Singleton._instances) == 0

        redislock1 = ClientRedisLocks()
        assert len(Singleton._instances) == 1
        assert 'ClientRedisLocks' in Singleton._instances

        redislock2 = ClientRedisLocksRenamed.ClientRedisLocks()
        assert len(Singleton._instances) == 1

        redislock3 = ClientRedisLocksRenamed2()
        assert len(Singleton._instances) == 1

    def test_chained_hierarchy(self, mock_env_no_servers):
        """
        creation of instances in a inheritance hierarchy should result in distinct classes
        """
        from EVECelery.clients.ClientRedis import ClientRedis, ClientRedisCache, ClientRedisLocks

        assert len(Singleton._instances) == 0

        base = ClientRedis('t', 't', 't', 1, 1)
        assert len(Singleton._instances) == 1
        assert 'ClientRedis' in Singleton._instances

        cache = ClientRedisCache()
        assert len(Singleton._instances) == 2
        assert 'ClientRedisCache' in Singleton._instances

        locks = ClientRedisLocks()
        assert len(Singleton._instances) == 3
        assert 'ClientRedisLocks' in Singleton._instances

    def test_get_same_instance_from_second_call(self, mock_env_no_servers):
        """
        secondary calls should not make new instances of an inherited singleton class
        resetting instance references should generate new classes
        """
        from EVECelery.clients.ClientRedis import ClientRedisLocks

        locks1 = ClientRedisLocks()
        locks2 = ClientRedisLocks()
        assert len(Singleton._instances) == 1
        assert 'ClientRedisLocks' in Singleton._instances
        assert id(locks1) == id(locks2)

        Singleton.clear_instance_references()
        assert len(Singleton._instances) == 0

        locks3 = ClientRedisLocks()
        assert len(Singleton._instances) == 1
        assert 'ClientRedisLocks' in Singleton._instances
        assert id(locks3) != id(locks1)

    def test_exception_dont_persist(self):
        """
        when creating class that has exception raised in init method don't cache the bad class
        """
        from EVECelery.clients.ClientRedis import ClientRedisLocks

        with pytest.raises(SystemExit):
            locks1 = ClientRedisLocks()

        assert len(Singleton._instances) == 0
        assert len(Singleton._init_locks) == 1
        assert len(Singleton._init_locks) == 1
        assert Singleton._init_locks['ClientRedisLocks'].locked() is False
