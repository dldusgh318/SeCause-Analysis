from redis import Redis
from rq import Queue

from app.core.config import settings


def get_redis_connection() -> Redis:
    return Redis.from_url(settings.REDIS_URL)


def get_analysis_queue() -> Queue:
    return Queue(
        name=settings.ANALYSIS_QUEUE_NAME,
        connection=get_redis_connection(),
    )
