from tests.TestUtils import *
import pytest
from EVECelery.clients.ClientRabbitMQ import *
from pika.exceptions import AMQPConnectionError, ProbableAuthenticationError


class TestClientRabbitMQ:
    def test_init_params(self):
        """
        provide params and ensure model has correct values
        """
        c = ClientRabbitMQ(user='testuser', password='testpass', host='localhost', port=1000, vhost='testvhost')
        assert c.config.user == 'testuser'
        assert c.config.password == 'testpass'
        assert c.config.host == 'localhost'
        assert c.config.port == 1000
        assert c.config.vhost == 'testvhost'

    def test_os_env_connect(self, mock_env_rabbitmq):
        """
        test connection is successful when setting os vars and initializing the client
        """
        c = ClientRabbitMQ()
        c.check_connection()

    def test_check_connection_bad_credentials(self, mock_env_rabbitmq):
        """
        Should raise exec when testing connection to a server with bad credentials
        """
        c = ClientRabbitMQ(user='testuser', password='testpass')
        with pytest.raises(ProbableAuthenticationError):
            c.check_connection()

    def test_check_connection_not_running(self):
        """
        Should raise exec when testing connection to a server that is not started
        """
        c = ClientRabbitMQ(user='testuser', password='testpass', host='localhost', port=1000, vhost='testvhost')
        with pytest.raises(AMQPConnectionError):
            c.check_connection()
