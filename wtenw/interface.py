from prompt_toolkit import PromptSession

from wtenw.helper.prompt import NotInStringListValidator, NumberValidator, TestCompleter, WelcomeValidator
from wtenw.picker.resolver import FOOD, DishPlan, add_dish_if_not_redundant, fetch_dishes_and_create_order


class Interface:
    def __init__(self):
        self.session = PromptSession()

    def welcome_prompt(self):
        action = self.session.prompt(
            (
                'Welcome to what-to-eat-next-week!\n\n'
                'You can\n'
                '    View available dishes (v)\n'
                '    Generate a meal plan (g) or\n'
                '    Add new dishes and items (a)\n'
            ),
            validator=WelcomeValidator(),
        )
        if action == 'v':
            self.view_dishes_prompt()
        elif action == 'g':
            self.plan_prompt()
        else:
            self.add_dishes_prompt()

    def view_dishes_prompt(self):
        print(fetch_dishes_and_create_order())

    def plan_prompt(self):
        # TODO Display plan and prompt for replacing items (by index)
        dishes = fetch_dishes_and_create_order()
        number = int(
            self.session.prompt(
                f'How many dishes do you want to plan? [1..{len(dishes)}]',
                validator=NumberValidator(max_value=len(dishes)),
            )
        )
        plan = DishPlan()
        for index, dish in enumerate(dishes):
            if index < number:
                add_dish_if_not_redundant(dish, plan)
            else:
                break
        print(plan.pretty_print())

    def add_dishes_prompt(self):
        # Either define dish, define major item or possibly delete dish?
        self._define_dish()
        pass

    def _define_dish(self):
        # Name dish
        dish_name = self.session.prompt(
            'What name should the dish have?',
            validator=NotInStringListValidator(string_list=fetch_dishes_and_create_order()),
        )
        # add major items
        items = []
        while True:
            item = self.session.prompt(
                f'Please name a major item for {dish_name}. Otherwise type x.',
                completer=TestCompleter(string_list=FOOD['ingredients'].keys()),
            )
            if item in ['x', 'X', 'x.', 'X.', ' X', ' x', 'x ', 'X ']:
                break
            items.append(item)
        print(dish_name, items)
