import pytest
import redis

from page_tracker.app import app


@pytest.fixture
def http_client():
    #app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture(scope="module")
def redis_client():
    return redis.Redis()

