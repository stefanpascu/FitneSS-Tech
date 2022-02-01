import pytest
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
    client = app.test_client()

    client.post("/auth/register", data={'username': 'test', 'password': 'test'})
    client.post("/auth/login", data={'username': 'test', 'password': 'test'})

    return client


def test_auth(client):
    response = client.post("/auth/register", data={'username': 'test_auth', 'password': 'test_auth'})
    assert response.status_code == 200
    response = client.post("/auth/login", data={'username': 'test_auth', 'password': 'test_auth'})
    assert response.status_code == 200


def test_set_bpm(client):
    response = client.post("/bpm", follow_redirects=True)
    assert response.status_code == 200


def test_get_bpm(client):
    response = client.get("/bpm", follow_redirects=True)
    assert response.status_code == 200


def test_set_steps(client):
    response = client.post("/steps", follow_redirects=True)
    assert response.status_code == 400
    response = client.post("/steps", data={"steps": 77}, follow_redirects=True)
    assert response.status_code == 201


def test_get_steps(client):
    response = client.get("/steps", follow_redirects=True)
    assert response.status_code == 200


def test_set_temperature(client):
    response = client.post("/temperature", follow_redirects=True)
    assert response.status_code == 400
    response = client.post("/temperature", data={"temp": 40}, follow_redirects=True)
    assert response.status_code == 201


def test_get_temperature(client):
    response = client.get("/temperature", follow_redirects=True)
    assert response.status_code == 200


def test_set_sleep(client):
    response = client.post("/sleep", data={"total": 7}, follow_redirects=True)
    assert response.status_code == 400
    response = client.post("/sleep", data={"rem": 2}, follow_redirects=True)
    assert response.status_code == 400
    response = client.post("/sleep", data={"total": 7, "rem": 2}, follow_redirects=True)
    assert response.status_code == 201


def test_get_sleep(client):
    response = client.get("/sleep", follow_redirects=True)
    assert response.status_code == 200


def test_set_theme(client):
    response = client.post("/theme", follow_redirects=True)
    assert response.status_code == 400
    response = client.post("/theme", data={"theme": "gray"}, follow_redirects=True)
    assert response.status_code == 400
    response = client.post("/theme", data={"theme": "dark"}, follow_redirects=True)
    assert response.status_code == 200


def test_get_theme(client):
    response = client.get("/theme", follow_redirects=True)
    assert response.status_code == 200


def test_get_status(client):
    response = client.get("/status", follow_redirects=True)
    assert response.status_code == 200
