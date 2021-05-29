import asyncpg

postgres: asyncpg.Connection = None


async def get_postgres() -> asyncpg.Connection:
    return postgres
