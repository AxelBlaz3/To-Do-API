from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import JSONResponse
from app.exceptions.task_not_found_exception import TaskNotFoundException
from app.routers import tasks
from app.database.todo_db import todo_db

app = FastAPI()

# Add event handlers for handling database connection.
app.add_event_handler("startup", todo_db.connect_to_todo_db)
app.add_event_handler("shutdown", todo_db.close_todo_db_connection)


# Add custom exception handlers
@app.exception_handler(TaskNotFoundException)
async def exception_handler(request: Request, exception: 'TaskNotFoundException'):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': f'Oops! Task not found.'})


# Include routers
app.include_router(router=tasks.router)
