import unittest.mock

import pytest
from redis import ConnectionError

from page_tracker.app import app

# def test_index_page(http_client):
#     response = http_client.get("/")
#     assert response.status_code == 200
#     assert b"This page has been seen" in response.data
#     assert b"1" in response.data

@unittest.mock.patch("page_tracker.app.redis")
def test_should_call_redis_incr(mock_redis, http_client):
    # Given
    # mock recis to return 5 for inct
    mock_redis.return_value.incr.return_value = 5

    # When
    response = http_client.get("/")

    # Then
    assert response.status_code == 200
    assert response.text == "This page has been seen 5 times."
    mock_redis.return_value.incr.assert_called_once_with("page_views")

@unittest.mock.patch("page_tracker.app.redis")
def test_should_handle_redis_connection_error(mock_redis, http_client):
    # Given
    mock_redis.return_value.incr.side_effect = ConnectionError

    # When
    response = http_client.get("/")

    # Then
    assert response.status_code == 500
    assert response.text == "Sorry, something went wrong \N{pensive face}"
    