from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError("expected at least 1 arguments, got 0")

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f"{{0:0{len(uniq_categories)}b}}"

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (
            int(b) for b in bin_format.format(1 << len(seen_categories))
        )
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_first():
    """
    Test for a single category.
    """
    assert fit_transform("SOS") == [("SOS", [1])]


def test_third():
    """
    Test for raising a TypeError with no arguments.
    """
    with pytest.raises(TypeError):
        fit_transform()


@pytest.mark.parametrize(
    "text, result",
    [(["I", "am", "who", "I", "am"],
        [
            ('I', [0, 0, 1]),
            ('am', [0, 1, 0]),
            ('who', [1, 0, 0]),
            ('I', [0, 0, 1]),
            ('am', [0, 1, 0]),
        ],),],)
def test_second(text, result):
    """
    Test for multiple categories.
    """
    assert fit_transform(text) == result


def test_fourth():
    assert fit_transform("Igor") == [('Igor', [1])]
