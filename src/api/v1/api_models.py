from pydantic import BaseModel
from uuid import UUID


class HelloWorldResponse(BaseModel):
    uuid: UUID
    hello: str
    world: str
