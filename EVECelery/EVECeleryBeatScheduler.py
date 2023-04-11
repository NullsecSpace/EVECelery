from .EVECeleryWorker import EVECeleryWorker


class EVECeleryBeatScheduler(EVECeleryWorker):
    """
    Celery beat scheduler for periodic tasks.

    """

    def schedule_task(self, schedule_name: str, schedule_config: dict):
        """Schedule a task to run at intervals. The passed in schedule object is a dictionary following the
        format and fields described here:
        https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#available-fields

        :param schedule_name: Name of the scheduled job. This must be unique.
        :param schedule_config: The scheduled job config as specified at
            https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#available-fields
        :return: None
        """
        self.beat_schedule[schedule_name] = schedule_config
        self.app.conf.update(beat_schedule=self.beat_schedule)

    def start(self):
        self.print_header()
        self.app.start(argv=["beat", "-l", self.worker_log_level])
