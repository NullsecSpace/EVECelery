from ESICelery import CeleryApp
from ESICelery.tasks.Character import *
import os


def main():
    c = CeleryApp(os.environ["BrokerUser"], os.environ["BrokerPassword"], os.environ["BrokerHost"],
                  int(os.environ["BrokerPort"]), os.environ["BrokerVhost"],
                  os.environ["ResultBackendUser"], os.environ["ResultBackendPassword"],
                  os.environ["ResultBackendHost"],
                  int(os.environ["ResultBackendPort"]), int(os.environ["ResultBackendDb"]),
                  os.environ["HeaderEmail"])

    r = CharacterPublicInfo().get_sync(timeout=5, character_id=1326083433)
    print(r)


if __name__ == '__main__':
    main()
