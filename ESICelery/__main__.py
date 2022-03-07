from ESICelery.CeleryApp import CeleryApp
import os


def main():
    try:
        c = CeleryApp(os.environ["BrokerUser"], os.environ["BrokerPassword"], os.environ["BrokerHost"],
                      int(os.environ["BrokerPort"]), os.environ["BrokerVhost"],
                      os.environ["ResultBackendUser"], os.environ["ResultBackendPassword"],
                      os.environ["ResultBackendHost"],
                      int(os.environ["ResultBackendPort"]), int(os.environ["ResultBackendDb"]),
                      os.environ["HeaderEmail"])
    except KeyError as ex:
        print("Environmental variable is not set.")
        raise ex
    c.start()


if __name__ == '__main__':
    main()
