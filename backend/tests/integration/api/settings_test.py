def test_settings_get_all(test_app):
    response = test_app.get("/settings")
    assert response.status_code == 200


def test_settings_create(test_app):
    response = test_app.post("/settings")
    assert response.status_code == 422


def test_settings_get_one(test_app):
    response = test_app.get("/settings/1")
    assert response.status_code == 404


def test_settings_delete(test_app):
    response = test_app.delete("/settings/1")
    assert response.status_code == 404
