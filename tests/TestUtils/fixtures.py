import pytest
import docker
import datetime as dt
import time
import random


@pytest.fixture(scope="session")
def docker_services_cleanup():
    """
    ensures all services created by unit tests are cleaned up before and after testing
    """
    client = docker.from_env()

    def kill_containers():
        for c in client.containers.list(filters={'label': 'EVECeleryTestFramework', 'status': 'running'}):
            c.kill()

    kill_containers()
    yield {}
    time.sleep(.5)
    kill_containers()


@pytest.fixture(scope='class')
def server_rabbitmq(docker_services_cleanup):
    client = docker.from_env()
    d = {'host': '127.0.0.1',
         'port': random.randint(14000, 15000),
         'user': 'EVECelery',
         'pass': 'EVECeleryPass',
         'vhost': 'EVECeleryVHost'
         }
    c = client.containers.run('rabbitmq:3-management',
                              auto_remove=True,
                              hostname='evecelerytests-rabbitmq',
                              environment={
                                  'RABBITMQ_DEFAULT_USER': d['user'],
                                  'RABBITMQ_DEFAULT_PASS': d['pass'],
                                  'RABBITMQ_DEFAULT_VHOST': d['vhost']
                              },
                              labels=[
                                  'EVECeleryTestFramework'
                              ],
                              ports={
                                  '5672/tcp': (d['host'], d['port'])
                              },
                              detach=True)

    start = dt.datetime.utcnow()
    while True:
        c.reload()
        if c.status == 'running' and 'Server startup complete' in str(c.logs(stream=False)):
            break
        if dt.datetime.utcnow() >= start + dt.timedelta(seconds=10):
            c.kill()
            raise Exception('RabbitMQ server container failed to start within the required time limit.')
        time.sleep(.25)
    yield d
    c.kill()


@pytest.fixture(scope='class')
def server_redis(docker_services_cleanup):
    d = {'host': '127.0.0.1',
         'port': random.randint(16000, 17000),
         'user': 'default',
         'pass': 'EVECelery'
         }
    client = docker.from_env()
    c = client.containers.run('redis:6',
                              auto_remove=True,
                              hostname='evecelerytests-redis',
                              command=f'--requirepass "{d["pass"]}" --appendonly yes --appendfsync everysec',
                              labels=[
                                  'EVECeleryTestFramework'
                              ],
                              ports={
                                  '6379/tcp': (d['host'], d['port'])
                              },
                              detach=True)

    start = dt.datetime.utcnow()
    while True:
        c.reload()
        if c.status == 'running' and 'Ready to accept connections' in str(c.logs(stream=False)):
            break
        if dt.datetime.utcnow() >= start + dt.timedelta(seconds=10):
            c.kill()
            raise Exception('Redis server container failed to start within the required time limit.')
        time.sleep(.25)
    yield d
    c.kill()

# @pytest.fixture(scope="function")
# def celery_config(broker, result_backend):
#     return {
#         'broker_url': "amqp://ESICelery:ESICeleryPass@localhost:5672/ESICeleryVHost",
#         'result_backend': f"redis://default:ESICelery@127.0.0.1:6379/1"
#     }
