import json
from pathlib import Path
from random import shuffle

FOOD = json.loads((Path(__file__).parent.parent / 'food' / 'food.json').read_text())


class DishPlan:
    def __init__(self):
        self.dishes = []
        self.major_items = []
        self.ingredients = []

    def add_dish(self, dish):
        self.dishes.append(dish)
        self.major_items.extend(FOOD['dishes'][dish])
        self.ingredients.extend(resolve_ingredients(dish))

    def pretty_print(self):
        return json.dumps(
            {
                'dishes': self.dishes,
                'ingredients': self.ingredients
             },
            indent=2
        )


class UnknownDish(Exception):
    pass


def add_dish_if_not_redundant(dish: str, plan: DishPlan) -> None:
    if dish not in FOOD['dishes']:
        raise UnknownDish(f'{dish} not found in list of known dishes')
    major_items = FOOD['dishes'][dish]
    if all(item not in plan.major_items for item in major_items):
        plan.add_dish(dish)


def fetch_dishes_and_create_order() -> list[str]:
    dishes = list(FOOD['dishes'].keys())
    shuffle(dishes)
    return dishes


def resolve_ingredients(dish: str) -> list[str]:
    if dish not in FOOD['dishes']:
        raise UnknownDish(f'{dish} not found in list of known dishes')
    ingredients = []
    for dish_part in FOOD['dishes'][dish]:
        if dish_part in FOOD['ingredients']:
            ingredients.extend(FOOD['ingredients'][dish_part])
        else:
            ingredients.append(dish_part)
    return ingredients
