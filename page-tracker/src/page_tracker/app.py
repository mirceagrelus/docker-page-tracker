"""
Sample Flask app.
https://realpython.com/docker-continuous-integration/#reader-comments
"""
from functools import cache
import os

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)
# redis = Redis()


@cache
def redis():
    """
    Returns a Redis client. The @cache creates a singleton.
    https://realpython.com/lru-cache-python/
    """
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))


@app.get("/")
def index():
    """
    Root route.
    Returns the number of times the page has been viewed.
    """
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return f"Sorry, something went wrong \N{pensive face}", 500
    return f"This page has been seen {page_views} times."
