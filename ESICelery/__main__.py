from ESICelery.CeleryApps import CeleryWorker, CeleryBeat
import sys


def main():
    if "--beat" not in sys.argv:
        celery_server = CeleryWorker
    else:
        celery_server = CeleryBeat
    try:
        c = celery_server.create_class()
    except KeyError as ex:
        print("Environmental variable is not set.")
        raise ex
    c.start()


if __name__ == '__main__':
    main()
