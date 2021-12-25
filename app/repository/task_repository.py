from typing import List
from fastapi.encoders import jsonable_encoder
from app.database.todo_db import todo_db
from app.exceptions.task_not_found_exception import TaskNotFoundException
from app.models.task import Task
import app.config
from app.database.todo_collections import TodoCollections
from app.models.update_task import UpdateTask


class TaskRepository:
    """Repository class for handling operations related to database."""

    @staticmethod
    async def create_task(task: Task, settings: app.config.Settings):
        """Creates a new task and inserts in database.

        Args:
            task (Task): The task to create.
        """
        db = settings.mongo_db
        task = jsonable_encoder(task)
        # Insert the task.
        task_result = await todo_db.client[db][TodoCollections.tasks].insert_one(task)
        # Get the created task from database and return it.
        created_task = await todo_db.client[db][TodoCollections.tasks].find_one({'_id': task_result.inserted_id})

        return created_task

    @staticmethod
    async def get_task(task_id: str, settings: app.config.Settings) -> Task:
        """Given a task id, return a task.

        Args:
            task_id (str): A valid ObjectId str.
            settings (app.config.Settings): Defaults to app.dependencies.get_settings.

        Returns:
            Task: Task for a given id. 
        """
        db = settings.mongo_db
        task = await todo_db.client[db][TodoCollections.tasks].find_one({'_id': task_id})

        # Raise TaskNotFoundException if task is None.
        if not task:
            raise TaskNotFoundException(task_id=task_id)
        return task

    @staticmethod
    async def get_tasks_for_user(user_id: str, settings: app.config.Settings) -> List[Task]:
        """Given user id, return list of tasks for the user.

        Args:
            user_id (str): A valid ObjectId str.
            settings (app.config.Settings): Defaults to app.dependencies.get_settings.

        Returns:
            List[Task]: Tasks of the user.
        """
        db = settings.mongo_db
        # Create an empty tasks list.
        tasks = []
        # Get the cursor.
        tasks_cursor = todo_db.client[db][TodoCollections.tasks].find(
            {'userId': user_id})
        # Loop over cursor and append each task to list.
        async for task in tasks_cursor:
            tasks.append(task)
        return tasks

    @staticmethod
    async def update_task(task_id: str, task: UpdateTask, settings: app.config.Settings):
        """Update a task.

        Args:
            task_id (str): The id of the task to update.
            settings (app.config.Settings): Defaults to app.dependencies.get_settings
        """
        db = settings.mongo_db
        # Filter out None attributes from task.
        task = {k: v for k, v in task.dict().items() if v is not None}

        task_update_result = await todo_db.client[db][TodoCollections.tasks].update_one({'_id': task_id}, {'$set': task})

        # Check if modified count is 1.
        if task_update_result.modified_count == 1:
            updated_task = await todo_db.client[db][TodoCollections.tasks].find_one({'_id': task_id})
            return updated_task

        # Either we don't have a task or the client sent the same task data as in database.
        # Let's check if latter is the case, if so, simply return the task. Raise TaskNotFoundException otherwise.
        # All this is logic is handled in get_task method.
        return await TaskRepository.get_task(task_id=task_id, settings=settings)
