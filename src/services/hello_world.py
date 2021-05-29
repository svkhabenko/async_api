import uuid
from functools import lru_cache

from aioredis import Redis
from asyncpg import Connection
from fastapi import Depends

from src.db.postgres import get_postgres
from src.db.redis import get_redis
from src.models.hello_world import HelloWorld


class HelloWorldService:
    def __init__(self, redis_client: Redis, postgres_client: Connection):
        self.redis_client = redis_client
        self.postgres_client = postgres_client

    async def get_some_data(self) -> HelloWorld:
        """ Какое-то действие, которое возвращает какую-то модель
        """
        await self.redis_client.ping()

        return HelloWorld(
            uuid=uuid.uuid4(),
            hello="hello",
            world="world",
        )


@lru_cache()
def get_hello_world_service(
        redis_client: Redis = Depends(get_redis),
        postgres_client: Connection = Depends(get_postgres),
) -> HelloWorldService:
    return HelloWorldService(redis_client, postgres_client)
