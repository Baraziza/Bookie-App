import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

def test_home_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_health_check():
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert response.json == {"status": "healthy"} 