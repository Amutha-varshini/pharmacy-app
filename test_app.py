from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Pharmacy Management System" in response.data

def test_inventory():
    client = app.test_client()
    response = client.get('/inventory')
    assert response.status_code == 200
    assert b"Paracetamol" in response.data
