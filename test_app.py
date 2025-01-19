
import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the home route
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Command and Control System is fully functional.' in response.data

# Test the encryption route
def test_encrypt(client):
    data = {"data": "Test message"}
    response = client.post('/encrypt', json=data)
    assert response.status_code == 200
    assert "encrypted_data" in response.get_json()

# Test the decryption route
def test_decrypt(client):
    data = {"data": "Test message"}
    encrypt_response = client.post('/encrypt', json=data)
    encrypted_data = encrypt_response.get_json()["encrypted_data"]

    decrypt_response = client.post('/decrypt', json={"encrypted_data": encrypted_data})
    assert decrypt_response.status_code == 200
    assert decrypt_response.get_json()["decrypted_data"] == "Test message"

# Test the OSINT route
def test_osint(client):
    response = client.get('/osint')
    assert response.status_code == 200
    assert "source" in response.get_json()
    assert "details" in response.get_json()
