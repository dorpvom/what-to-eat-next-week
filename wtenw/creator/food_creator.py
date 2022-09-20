class RedundantFood(Exception):
    pass


class UnknownItem(Exception):
    pass


def add_new_dish(known_food: dict, dish_name: str, major_items: list[str]) -> dict:
    if dish_name in known_food['dishes']:
        raise RedundantFood(f'Dish {dish_name} already in food database')
    known_food[dish_name] = major_items
    return known_food


def define_major_item(known_food: dict, major_item: str, ingredients: list[str]) -> dict:
    if major_item in known_food['ingredients']:
        raise RedundantFood(f'Major item {major_item} already in food database')
    if not any(major_item in major_items for _, major_items in known_food['dishes'].items()):
        raise UnknownItem(f'Major item {major_item} is not used in any dish. Check for typos')
    known_food['ingredients'][major_item] = ingredients
    return known_food
