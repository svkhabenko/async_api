import asyncpg
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api.utils import health_check
from src.api.v1 import hello_world
from src.core.settings import Settings
from src.db import redis, postgres
import aioredis

ENV_FILE = "../.env"

settings = Settings(_env_file=ENV_FILE)

app = FastAPI(
    title="Пример API",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    description="Хэллоу ворлд на максималках",
    version="1.0.0"
)

app.include_router(hello_world.router, prefix="/api/v1/hello_world", tags=["Hello World"])
app.include_router(health_check.router, prefix="/api", tags=["health"])


@app.on_event("startup")
async def startup():
    redis.redis = await aioredis.create_redis_pool(settings.redis_dsn)
    postgres.postgres = await asyncpg.connect(
        user=settings.postgres_user,
        password=settings.postgres_password,
        database=settings.postgres_database,
        host=settings.postgres_host,
        port=settings.postgres_port,
    )


@app.on_event("shutdown")
async def shutdown():
    await redis.redis.close()
    await postgres.postgres.close()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level,
        debug=settings.debug,
    )
