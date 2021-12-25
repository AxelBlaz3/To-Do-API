from fastapi import APIRouter, status
from fastapi.param_functions import Body
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from app.config import Settings
from app.models.task import Task
import app.dependencies
from app.models.update_task import UpdateTask
from app.repository.task_repository import TaskRepository

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.get('/', name='Get all tasks for given user id')
async def get_tasks(user_id: str):
    return []


@router.post('/', response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: Task = Body(...), settings: Settings = Depends(app.dependencies.get_settings)):
    created_task = await TaskRepository.create_task(task=task, settings=settings)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_task)


@router.get('/user/{user_id}', name='Get tasks of a user.')
async def get_tasks_of_user(user_id: str, token: str = Depends(app.dependencies.oauth2_scheme), settings: Settings = Depends(app.dependencies.get_settings)):
    tasks = await TaskRepository.get_tasks_for_user(user_id=user_id, settings=settings)
    # return {'token': token}
    return tasks


@router.get('/{task_id}', name='Get task by id.',)
async def get_task(task_id: str, settings: Settings = Depends(app.dependencies.get_settings)):
    task = await TaskRepository.get_task(task_id=task_id, settings=settings)
    return task


@router.put('/{task_id}', name='Update a task.')
async def update_task(task_id: str, task: UpdateTask = Body(...), settings: Settings = Depends(app.dependencies.get_settings)):
    task = await TaskRepository.update_task(task_id=task_id, task=task, settings=settings)
    return task    