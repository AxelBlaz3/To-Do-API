from enum import Enum


class TodoCollections(str, Enum):
    """ Enum to hold collection names."""
    tasks = "tasks"
    users = "users"
    completedTasks = "completedTasks"
