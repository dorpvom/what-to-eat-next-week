import json
from pathlib import Path

FOOD = json.loads((Path(__file__).parent.parent / 'food' / 'food.json').read_text())

class UnknownDish(Exception):
    pass


def resolve_ingredients(dish: str) -> list[str]:
    if not dish in FOOD['dishes']:
        raise UnknownDish(f'{dish} not found in list of known dishes')
    ingredients = []
    for dish_part in FOOD['dishes'][dish]:
        if dish_part in FOOD['ingredients']:
            ingredients.extend(FOOD['ingredients'][dish_part])
        else:
            ingredients.append(dish_part)
    return ingredients