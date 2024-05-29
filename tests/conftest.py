import pytest
from database_app import app as my_app


@pytest.fixture()
def app():
    app = my_app
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()

