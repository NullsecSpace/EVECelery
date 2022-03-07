import platform
import requests
import ESIRabbit.config
from ESIRabbit.exceptions.utils import MissingHeaderEmail


class RequestHeaders(object):
    @classmethod
    def get_email(cls):
        if ESIRabbit.config.header_email is None:
            raise MissingHeaderEmail("Missing 'header_email' variable. "
                                     "Please set this variable to your email address so ESI and ZK APIs "
                                     "can contact you if there are problems. "
                                     "Requests to ESI or ZK will not occur until this field is set.")
        else:
            return ESIRabbit.config.header_email

    @classmethod
    def get_headers(cls) -> dict:
        h = {"Accept":      "application/json",
             "From":        cls.get_email(),
             "Maintainer":  "maintainers@eveinsight.net",
             "User-Agent":  f"ESIRabbit {ESIRabbit.config.version} (https://github.com/EVEInsight/ESIRabbit)"
                            f"Python/{platform.python_version()} "
                            f"Requests/{requests.__version__}"}
        return h
