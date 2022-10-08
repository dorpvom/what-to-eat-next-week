from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.sqlite import BOOLEAN, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

# pylint: disable=too-few-public-methods

Base = declarative_base()

DishItem = Table(
    'DishItem',
    Base.metadata,
    Column('dish', ForeignKey('dish.name')),
    Column('item', ForeignKey('major_item.name')),
)

ItemIngredient = Table(
    'ItemIngredient',
    Base.metadata,
    Column('item', ForeignKey('major_item.name')),
    Column('ingredient', ForeignKey('ingredient.name')),
)


class Dish(Base):
    __tablename__ = 'dish'

    name = Column(VARCHAR, primary_key=True)
    items = relationship('MajorItem', secondary=DishItem)

    def __repr__(self) -> str:
        return f'Dish({self.name})'


class MajorItem(Base):
    __tablename__ = 'major_item'

    name = Column(VARCHAR, primary_key=True)
    ingredients = relationship('Ingredient', secondary=ItemIngredient)

    def __repr__(self) -> str:
        return f'MajorItem({self.name}, {self.ingredients})'


class Ingredient(Base):
    __tablename__ = 'ingredient'

    name = Column(VARCHAR, primary_key=True)
    sugar = Column(BOOLEAN)
    carb = Column(BOOLEAN)
    meat = Column(BOOLEAN)

    def __repr__(self) -> str:
        return f'Ingredient({self.name})'
