import urllib.request
import json
import pytest
from unittest.mock import patch

API_URL = "http://worldclockapi.com/api/json/utc/now"

YMD_SEP = "-"
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = "."
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json["currentDateTime"]
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError("Unexpected format")

    return int(year_str)


def test_value_error():
    with patch("urllib.request.urlopen"), patch(
        "json.load"
    ) as mocked_load, pytest.raises(Exception):
        mocked_load["currentDateTime"] = -1
        what_is_year_now()


def test_first_if():
    with patch("urllib.request.urlopen"), patch("json.load") as mocked_load:
        mocked_load.return_value = {"currentDateTime": "0000-"}
        assert what_is_year_now() == 0


def test_elif():
    with patch("urllib.request.urlopen"), patch("json.load") as mocked_load:
        mocked_load.return_value = {"currentDateTime": "......0000"}
        assert what_is_year_now() == 0
