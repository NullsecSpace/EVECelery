import os
import platform
import requests
from EVECelery.exceptions.utils import MissingHeaderEmail
from EVECelery import __version__


class RequestHeaders(object):
    @classmethod
    def get_email(cls):
        email = os.environ.get('EVECelery_Email')
        if email is None:
            raise MissingHeaderEmail("Missing 'header_email' variable. "
                                     "Please set this variable to your email address so ESI and ZK APIs "
                                     "can contact you if there are problems. "
                                     "Requests to ESI or ZK will not occur until this field is set.")
        else:
            return email

    @classmethod
    def get_headers(cls) -> dict:
        h = {"Accept":      "application/json",
             "From":        cls.get_email(),
             "Maintainer":  "maintainers@nullsec.space",
             "User-Agent": f"EVECelery {__version__} (https://github.com/NullsecSpace/EVECelery)"
                           f"Python/{platform.python_version()} "
                           f"Requests/{requests.__version__}"}
        return h
