from base64 import b64encode

import pytest
import json
from app import create_app

import os
import tempfile
import db

os.chdir('..')

@pytest.fixture(scope="session", autouse=True)
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(db_path=db_path)

    with app.app_context():
        db.close_db()
        db.init_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()

def test_register(client):
    request = client.post("/auth/register", data={'username': 'test', 'password': 'test'})
    assert request.status_code == 200

def test_login(client):
    request = client.post("/auth/login", data={'username': 'test', 'password': 'test'})
    assert request.status_code == 200


# def test_get_temperature(client):
#     credentials = b64encode(b"test:test")
#     request = client.get("/temperature")
#     assert request.status_code == 405
#
#
# def test_set_temperature(client):
#     payload = {'temp': 100}
#     rv = client.post('/temperature', data=payload, follow_redirects=True)
#     res = json.loads(rv.data.decode())
#     assert rv.status_code == 200
#     assert res["status"] == "Temperature succesfully recorded"
