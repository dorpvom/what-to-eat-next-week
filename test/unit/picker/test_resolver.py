from pathlib import Path
from wtenw.picker.resolver import resolve_ingredients


import pytest
import json

@pytest.fixture(scope='function')
def food_list():
    return json.loads((Path(__file__).parent.parent / 'data' / 'food.json').read_text())


def test_resolve_ingredients():
    ingredients = resolve_ingredients('bratwurst mit pueree und kohlrabi')
    assert len(ingredients) == 11
    assert all(
        ingredient in ingredients for ingredient in
        ['bratwurst', 'kartoffel', 'suesskartoffel', 'milch', 'butter', 'muskatnuss', 'kohlrabi', 'zwiebel', 'sahne', 'mehl', 'bruehpulver']
    )
