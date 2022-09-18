from pathlib import Path
from wtenw.picker.resolver import (
    resolve_ingredients,
    fetch_dishes_and_create_order,
    DishPlan,
    add_dish_if_not_redundant,
)

import pytest
import json


@pytest.fixture(scope='function')
def food_list():
    return json.loads((Path(__file__).parent.parent / 'data' / 'food.json').read_text())


@pytest.fixture(scope='function', autouse=True)
def set_test_food(monkeypatch, food_list):
    monkeypatch.setattr('wtenw.picker.resolver.FOOD', food_list)


def test_resolve_ingredients():
    ingredients = resolve_ingredients('bratwurst mit pueree und kohlrabi')
    assert len(ingredients) == 11
    assert all(
        ingredient in ingredients
        for ingredient in [
            'bratwurst',
            'kartoffel',
            'suesskartoffel',
            'milch',
            'butter',
            'muskatnuss',
            'kohlrabi',
            'zwiebel',
            'sahne',
            'mehl',
            'bruehpulver',
        ]
    )


def test_fetch_dishes_and_create_order(food_list):
    dish_order = fetch_dishes_and_create_order()
    assert all(dish in dish_order for dish in food_list['dishes'])


def test_add_dish_if_not_redundant(food_list):
    plan = DishPlan()
    dish = 'bratwurst mit pueree und kohlrabi'

    add_dish_if_not_redundant(dish, plan)
    assert len(plan.dishes) == 1

    add_dish_if_not_redundant(dish, plan)
    assert len(plan.dishes) == 1

    similar_dish = 'frikadellen mit pueree'
    add_dish_if_not_redundant(similar_dish, plan)
    assert len(plan.dishes) == 1

    different_dish = 'tortellini alla panna'
    add_dish_if_not_redundant(different_dish, plan)
    assert len(plan.dishes) == 2
