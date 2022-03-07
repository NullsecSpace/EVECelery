from ESIRabbit import CeleryApp
from ESIRabbit.tasks.Character import *
import os


def main():
    c = CeleryApp(os.environ["BrokerUser"], os.environ["BrokerPassword"], os.environ["BrokerHost"],
                  os.environ["BrokerPort"], os.environ["BrokerVhost"],
                  os.environ["ResultBackendUser"], os.environ["ResultBackendPassword"],
                  os.environ["ResultBackendHost"],
                  os.environ["ResultBackendPort"], os.environ["ResultBackendDb"],
                  os.environ["HeaderEmail"])

    r = CharacterPublicInfo().get_sync(timeout=5, character_id=1326083433)
    print(r)


if __name__ == '__main__':
    main()
