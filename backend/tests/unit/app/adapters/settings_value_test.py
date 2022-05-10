from backend.app.common.adapters.settings import SettingsValueAdapter
from backend.app.enums.setting import MeasurementType


def test_adapt_to_millimeters():
    adapter = SettingsValueAdapter()
    expected = 0.001
    result = adapter.adapt_value_by_measurement(1, MeasurementType.MILLIMETERS.value)
    assert result == expected


def test_adapt_to_precentage():
    adapter = SettingsValueAdapter()
    expected = 0.01
    result = adapter.adapt_value_by_measurement(1, MeasurementType.PRECENTAGE.value)
    assert result == expected


def test_adapt_to_none():
    adapter = SettingsValueAdapter()
    expected = 1
    result = adapter.adapt_value_by_measurement(1, "")
    assert result == expected
