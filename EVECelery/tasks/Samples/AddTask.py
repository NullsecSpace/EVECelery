from EVECelery.tasks.BaseTasks.BaseTask import BaseTask


class AddTask(BaseTask):
    def run(self, a, b):
        return a + b
