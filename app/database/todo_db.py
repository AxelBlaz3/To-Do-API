from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
import app.dependencies


class TodoDatabase:
    """ TodoDatabase class for managing database client connections."""
    client: Optional[AsyncIOMotorClient] = None

    def get_db(self) -> AsyncIOMotorClient:
        return self.client

    async def connect_to_todo_db(self) -> None:
        """Establish a database connection."""
        self.client = AsyncIOMotorClient(
            app.dependencies.get_settings().mongodb_uri)

    async def close_todo_db_connection(self) -> None:
        """Close database connection."""
        self.client.close()


todo_db = TodoDatabase()
