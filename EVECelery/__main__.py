from EVECelery.CeleryApps import CeleryWorker, CeleryBeat
import sys


def main():
    if "--beat" not in sys.argv:
        celery_server = CeleryWorker
    else:
        celery_server = CeleryBeat

    c = celery_server(connection_check=True)
    c.start()


if __name__ == '__main__':
    main()
