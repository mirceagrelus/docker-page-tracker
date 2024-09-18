import pytest
import redis

from page_tracker.app import app

def pytest_addoption(parser):
    """
    Add command line options for the Flask and Redis URLs.
    This will allow us to run end to end tests by specifying the URLs:
    `python -m pytest -v test/e2e/ --flask-url http://127.0.0.1:8080 --redis-url redis://127.0.0.1:6379`
    """
    parser.addoption("--flask-url")
    parser.addoption("--redis-url")

@pytest.fixture(scope="session")
def flask_url(request):
    return request.config.getoption("--flask-url")

@pytest.fixture(scope="session")
def redis_url(request):
    return request.config.getoption("--redis-url")


@pytest.fixture
def http_client():
    #app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture(scope="module")
def redis_client(redis_url):
    """
    The Redis client fixture, which fixture now takes advantage of the optional Redis URL
    """
    if redis_url:
        return redis.Redis.from_url(redis_url)
    return redis.Redis()

