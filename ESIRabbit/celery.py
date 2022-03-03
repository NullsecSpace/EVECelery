from celery import Celery


app = Celery("ESIRabbit")
app.config_from_object("ESIRabbit.celeryconfig")


def main():
    """entry point to celery app"""
    app.start()


if __name__ == '__main__':
    main()
