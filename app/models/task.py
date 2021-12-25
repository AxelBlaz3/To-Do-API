from typing import List, Optional
from bson.objectid import ObjectId
from pydantic import BaseModel
from datetime import datetime
from pydantic import Field
from humps import camelize
from app.models.py_object_id import PyObjectId


class Task(BaseModel):
    """Task model."""
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    user_id: PyObjectId = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    notify_at: Optional[datetime] = Field(default=None)
    created_at: datetime = Field(default=datetime.utcnow())
    modified_at: datetime = Field(default=datetime.utcnow())
    category: str = Field(...)
    parent_task_id: Optional[PyObjectId] = Field(default=None)
    is_complete: bool = Field(default=False)
    sub_tasks: list = Field(default=[])

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
