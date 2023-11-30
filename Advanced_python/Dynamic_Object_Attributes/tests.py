import json
from advert import Advertisement
import pytest

lesson_str = """{
        "title": "python",
        "category": "programming",
        "cost": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"],
            "nested": {
                "four": "two"
                }
            }
        }"""
lesson = json.loads(lesson_str)
lesson_ad = Advertisement(lesson)


def test_attributes() -> None:
    """
    Test dynamic attributes creation.

    Checks that the dynamic attributes of
    the Advertisement class are created correctly.
    """
    assert lesson_ad.location.address == 'город Москва, Лесная, 7'
    assert lesson_ad.title == 'python'
    assert lesson_ad.location.nested.four == 'two'
    assert lesson_ad.category == 'programming'


def test_cost() -> None:
    """
    Test cost functionality.

    Checks the functionality related to the cost attribute
    of the Advertisement class.
    """
    assert lesson_ad.cost == 0
    assert Advertisement({"title": "qwe"}).cost == 0
    with pytest.raises(ValueError):
        Advertisement({'title': 'bad_cost', 'cost': 'two hundred'})
    with pytest.raises(ValueError):
        Advertisement({'title': 'bad_cost', 'cost': -100})
    with pytest.raises(ValueError):
        lesson_ad.cost = -15
    lesson_ad.cost = 15
    assert lesson_ad.cost == 15


def test_title() -> None:
    """
    Check that error raised if title not passed.

    Ensures that an error is raised when the title is not
    passed in the Advertisement constructor.
    """
    with pytest.raises(ValueError):
        Advertisement({"name": "Bob"})
