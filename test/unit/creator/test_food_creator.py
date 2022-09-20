from pathlib import Path
from wtenw.creator.food_creator import (
    add_new_dish,
    define_major_item,
    RedundantFood,
    UnknownItem,
)

import pytest
import json


@pytest.fixture(scope='function')
def food_list():
    return json.loads((Path(__file__).parent.parent / 'data' / 'food.json').read_text())


@pytest.fixture(scope='function', autouse=True)
def set_test_food(monkeypatch, food_list):
    monkeypatch.setattr('wtenw.picker.resolver.FOOD', food_list)


def test_add_new_dish(food_list):
    with pytest.raises(RedundantFood):
        add_new_dish(food_list, 'tortellini alla panna', ['some', 'items'])

    assert 'nuggets mit pommes' not in food_list['dishes']
    food_list_with_nuggets = add_new_dish(food_list, 'nuggets mit pommes', ['nuggets', 'pommes', 'frittierfett'])
    assert 'nuggets mit pommes' in food_list_with_nuggets


def test_define_major_item(food_list):
    assert 'tortellini' not in food_list['ingredients']
    food_list_with_tortellini = define_major_item(food_list, 'tortellini', ['some', 'ingredients'])
    assert 'tortellini' in food_list_with_tortellini['ingredients']

    with pytest.raises(RedundantFood):
        define_major_item(food_list_with_tortellini, 'tortellini', ['some', 'ingredients'])

    with pytest.raises(UnknownItem):
        define_major_item(food_list, 'unknown_item', ['some', 'ingredients'])
