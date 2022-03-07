from ESIRabbit import CeleryApp
from ESIRabbit.tasks.Universe import *
import os


def main():
    c = CeleryApp(os.environ["BrokerUser"], os.environ["BrokerPassword"], os.environ["BrokerHost"],
                  int(os.environ["BrokerPort"]), os.environ["BrokerVhost"],
                  os.environ["ResultBackendUser"], os.environ["ResultBackendPassword"],
                  os.environ["ResultBackendHost"],
                  int(os.environ["ResultBackendPort"]), int(os.environ["ResultBackendDb"]),
                  os.environ["HeaderEmail"])

    r = SystemInfo().get_sync(timeout=5, system_id=30000142)
    print(r)


if __name__ == '__main__':
    main()
