from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from app.router import router as router_operation
from tasks.router import router as router_tasks

app = FastAPI(
    title="Example App"
)

app.include_router(router_operation)
app.include_router(router_tasks)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

a= 3