"""
Unit tests for the Flask application.
Tests all endpoints: /, /health, and /data
"""
import pytest
import json
import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the homepage route returns 200 and contains expected content."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Flask app' in response.data
    assert b'text/html' in response.content_type.encode()


def test_health(client):
    """Test the health check endpoint returns OK status."""
    response = client.get('/health')
    assert response.status_code == 200
    assert b'OK' in response.data or b'ok' in response.data
    
    # Check JSON response structure
    json_data = response.get_json()
    assert json_data is not None
    assert 'status' in json_data
    assert json_data['status'] == 'ok'


def test_data_post_valid(client):
    """Test POST /data with valid JSON payload."""
    payload = {"name": "test", "value": 123}
    response = client.post(
        '/data',
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert response.status_code == 201
    
    json_data = response.get_json()
    assert 'received' in json_data
    assert json_data['received'] == payload
    assert 'message' in json_data


def test_data_post_invalid_content_type(client):
    """Test POST /data with non-JSON content type."""
    response = client.post(
        '/data',
        data='not json',
        content_type='text/plain'
    )
    assert response.status_code == 400
    
    json_data = response.get_json()
    assert 'error' in json_data


def test_data_post_empty_json(client):
    """Test POST /data with empty JSON payload."""
    response = client.post(
        '/data',
        data='',
        content_type='application/json'
    )
    assert response.status_code == 400


def test_data_get_method_not_allowed(client):
    """Test that GET method is not allowed on /data endpoint."""
    response = client.get('/data')
    assert response.status_code == 405  # Method Not Allowed


def test_invalid_route(client):
    """Test that invalid routes return 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404
