class TaskNotFoundException(Exception):
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id
