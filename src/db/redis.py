import aioredis

redis: aioredis.Redis = None


# Функция понадобится при внедрении зависимостей
async def get_redis() -> aioredis.Redis:
    return redis