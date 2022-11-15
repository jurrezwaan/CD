import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello, world!"


def test_cat(client):
    response = client.get("/cat")

    assert response.status_code == 200
    assert response.data == b"Miauw!"


def test_succes(client):
    response = client.get("/succes")

    assert response.status_code == 200
    assert response.data == b"Succes!"
