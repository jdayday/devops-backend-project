import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test that the home page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"DevOps Project API" in response.data

def test_health(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data