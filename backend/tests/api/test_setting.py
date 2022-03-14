import os
import pytest

from tests.conftest import test_app

ENDPOINT = "/settings"

def test_settings_get(test_app):
    response = test_app.get(ENDPOINT)
    assert response.status_code == 200