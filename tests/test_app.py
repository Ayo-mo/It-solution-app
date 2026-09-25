import pytest

from app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_services_page(client):
    response = client.get("/services")
    assert response.status_code == 200


def test_contact_page(client):
    response = client.get("/contact")
    assert response.status_code == 200


def test_admin_contacts_page(client):
    response = client.get("/admin/contacts")
    assert response.status_code == 200
