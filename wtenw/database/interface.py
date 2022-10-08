from wtenw.database.database import SQLDatabase
from wtenw.database.schema import Dish, Ingredient, MajorItem


class FoodInterface(SQLDatabase):
    def add_ingredient(self, name, sugar=False, carb=False, meat=False) -> None:
        with self.get_read_write_session() as session:
            ingredient = Ingredient(name=name, sugar=sugar, carb=carb, meat=meat)
            session.add(ingredient)

    def add_major_item(self, name, ingredients) -> None:
        with self.get_read_write_session() as session:
            ingredient_objects = []
            for ingredient in ingredients:
                if self.ingredient_exists(ingredient):
                    ingredient_object = self.get_ingredient(ingredient, session)
                else:
                    self.add_ingredient(ingredient)
                    ingredient_object = self.get_ingredient(ingredient, session)
                ingredient_objects.append(ingredient_object)

            major_item = MajorItem(name=name, ingredients=ingredient_objects)
            session.add(major_item)

    def ingredient_exists(self, ingredient) -> bool:
        with self.get_read_write_session() as session:
            return bool(session.get(Ingredient, ingredient))

    @staticmethod
    def get_ingredient(ingredient, session) -> Ingredient:
        return session.get(Ingredient, ingredient)

    @staticmethod
    def get_major_item(item, session) -> MajorItem:
        return session.get(MajorItem, item)

    def add_dish(self, name, major_items) -> None:
        with self.get_read_write_session() as session:
            item_objects = []
            for item in major_items:
                if self.major_item_exists(item):
                    item_object = self.get_major_item(item, session)
                else:
                    self.add_major_item(item, [])
                    item_object = self.get_major_item(item, session)
                item_objects.append(item_object)

            dish = Dish(name=name, items=item_objects)
            session.add(dish)

    def major_item_exists(self, major_item) -> bool:
        with self.get_read_write_session() as session:
            return bool(session.get(MajorItem, major_item))

    def set_ingredient_properties(self, name, sugar=False, carb=False, meat=False):
        pass

    def specify_major_item(self, name, ingredients):
        pass
