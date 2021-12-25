from typing import List, Optional
from bson.objectid import ObjectId
from pydantic import BaseModel
from datetime import datetime
from pydantic import Field
from humps import camelize
from app.models.py_object_id import PyObjectId


class UpdateTask(BaseModel):
    """UpdateTask model."""
    user_id: Optional[PyObjectId]
    title: Optional[str]
    description: Optional[str]
    notify_at: Optional[datetime]
    created_at: Optional[datetime]
    modified_at: Optional[datetime]
    category: Optional[str]
    parent_task_id: Optional[PyObjectId]
    is_complete: Optional[bool]
    sub_tasks: Optional[list]

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "61bada5fb59233282bee700f",
                "userId": "61b59b013335f0e0c142f7da",
                "title": "Grab a coffee",
                "description": "Need to hangout and grab a coffee.",
                "notifyAt": "2021-12-16T06:19:06.962893",
                "createdAt": "2021-12-16T06:19:06.962893",
                "modifiedAt": "2021-12-16T06:19:06.962893",
                "category": "Hangout",
                "parentTaskId": None,
                "isComplete": False,
                "subTasks": []
            }
        }
