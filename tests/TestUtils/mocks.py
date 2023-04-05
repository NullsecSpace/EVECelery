import pytest
import random
from .fixtures import server_rabbitmq, server_redis
from EVECelery.tasks.BaseTasks.BaseTask import BaseTask
from EVECelery.tasks.Alliance import *
from EVECelery.tasks.Character import *
from EVECelery.tasks.Corporation import *
from EVECelery.tasks.Market import *
from EVECelery.tasks.Routes import *
from EVECelery.tasks.Universe import *
from EVECelery.tasks.Samples import *


def fake_rabbitmq_connection_vars() -> dict:
    return {
        'EVECelery_RabbitMQ_User': 'user',
        'EVECelery_RabbitMQ_Password': 'pass',
        'EVECelery_RabbitMQ_Host': 'localhost',
        'EVECelery_RabbitMQ_Port': random.randint(14000, 15000),
        'EVECelery_RabbitMQ_Vhost': 'vhost1',
    }


def fake_redis_connection_vars() -> dict:
    return {
        'EVECelery_Redis_ResultBackend_User': 'user',
        'EVECelery_Redis_ResultBackend_Password': 'pass',
        'EVECelery_Redis_ResultBackend_Host': 'localhost',
        'EVECelery_Redis_ResultBackend_Port': random.randint(16000, 17000),
        'EVECelery_Redis_ResultBackend_DB': 1
    }


@pytest.fixture(scope='function')
def mock_env_no_servers(monkeypatch):
    """
    Sets env vars for connections but does not start RabbitMQ or Redis
    """
    env_vars = {
        **fake_rabbitmq_connection_vars(),
        **fake_redis_connection_vars()
    }
    for k, v in env_vars.items():
        monkeypatch.setenv(k, v)
    yield env_vars


@pytest.fixture(scope='function')
def mock_env_rabbitmq_redis(monkeypatch, server_rabbitmq, server_redis):
    """
    Starts a single RabbitMQ and single Redis node and associated variables for connections
    """
    env_vars = {
        'EVECelery_RabbitMQ_User': server_rabbitmq['user'],
        'EVECelery_RabbitMQ_Password': server_rabbitmq['pass'],
        'EVECelery_RabbitMQ_Host': server_rabbitmq['host'],
        'EVECelery_RabbitMQ_Port': server_rabbitmq['port'],
        'EVECelery_RabbitMQ_Vhost': server_rabbitmq['vhost'],
        'EVECelery_Redis_ResultBackend_User': server_redis['user'],
        'EVECelery_Redis_ResultBackend_Password': server_redis['pass'],
        'EVECelery_Redis_ResultBackend_Host': server_redis['host'],
        'EVECelery_Redis_ResultBackend_Port': server_redis['port'],
        'EVECelery_Redis_ResultBackend_DB': 1
    }
    for k, v in env_vars.items():
        monkeypatch.setenv(k, v)
    yield env_vars


@pytest.fixture(scope='function')
def mock_env_redis(monkeypatch, server_redis):
    """
    Starts a single Redis node and associated variables for the connection and fake variables for RabbitMQ.
    """
    env_vars = {
        **fake_rabbitmq_connection_vars(),
        'EVECelery_Redis_ResultBackend_User': server_redis['user'],
        'EVECelery_Redis_ResultBackend_Password': server_redis['pass'],
        'EVECelery_Redis_ResultBackend_Host': server_redis['host'],
        'EVECelery_Redis_ResultBackend_Port': server_redis['port'],
        'EVECelery_Redis_ResultBackend_DB': 1
    }
    for k, v in env_vars.items():
        monkeypatch.setenv(k, v)
    yield env_vars


@pytest.fixture(scope='function')
def celery_config(mock_env_rabbitmq_redis):
    return {
        'broker_url': f"amqp://{mock_env_rabbitmq_redis['EVECelery_RabbitMQ_User']}:{mock_env_rabbitmq_redis['EVECelery_RabbitMQ_Password']}@{mock_env_rabbitmq_redis['EVECelery_RabbitMQ_Host']}:{mock_env_rabbitmq_redis['EVECelery_RabbitMQ_Port']}/{mock_env_rabbitmq_redis['EVECelery_RabbitMQ_Vhost']}",
        'result_backend': f"redis://{mock_env_rabbitmq_redis['EVECelery_Redis_ResultBackend_User']}:{mock_env_rabbitmq_redis['EVECelery_Redis_ResultBackend_Password']}@{mock_env_rabbitmq_redis['EVECelery_Redis_ResultBackend_Host']}:{mock_env_rabbitmq_redis['EVECelery_Redis_ResultBackend_Port']}/{mock_env_rabbitmq_redis['EVECelery_Redis_ResultBackend_DB']}"
    }


@pytest.fixture(scope='function')
def celery_register_tasks(celery_config, celery_app):
    for t in BaseTask.get_all_subtasks():
        celery_app.register_task(t())
    return celery_app


@pytest.fixture(scope='function')
def mock_env_celery(monkeypatch, celery_register_tasks, celery_worker):
    monkeypatch.setenv('EVECelery_Email', 'testsuite@nullsec.space')
    yield
