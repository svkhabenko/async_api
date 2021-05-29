from uuid import UUID

from pydantic import BaseModel


class HelloWorld(BaseModel):
    uuid: UUID
    hello: str
    world: str
