class BaseClient(object):
    def check_connection(self) -> bool:
        """
        Check that a connection is successful, else raise exception
        """
        raise NotImplementedError

    @property
    def connection_str(self) -> str:
        """
        Returns the connection string for use by Celery
        """
        raise NotImplementedError
