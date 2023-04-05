from EVECelery import EVECeleryWorker, EVECeleryBeatScheduler
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='EVECelery',
        description='EVECelery is a distributed task queue framework for building tools that interact with the '
                    'EVE Online ESI API using Celery, RabbitMQ, and Redis.',
        epilog='This is the command-line interface for starting the EVECelery worker or beat scheduler service.')

    parser.add_argument('--beat', dest='beat', action='store_true', required=False,
                        help='Start and run the Celery beat scheduler instead of the Celery worker node.')
    args = parser.parse_args()
    if not args.beat:
        celery_server = EVECeleryWorker
    else:
        celery_server = EVECeleryBeatScheduler

    c = celery_server(connection_check=True)
    c.start()


if __name__ == '__main__':
    main()
