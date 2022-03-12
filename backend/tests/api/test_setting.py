from tests.conftest import test_app

def test_get_settings(test_app):
    response = test_app.get("/settings")
    assert response.status_code == 200

