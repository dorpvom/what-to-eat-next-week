from prompt_toolkit import PromptSession

from wtenw.helper.prompt import WelcomeValidator, NumberValidator
from wtenw.picker.resolver import FOOD, fetch_dishes_and_create_order, add_dish_if_not_redundant, DishPlan


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
            validator=WelcomeValidator()
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
        dishes = fetch_dishes_and_create_order()
        number = int(
            self.session.prompt(
                f'How many dishes do you want to plan? [1..{len(dishes)}]',
                validator=NumberValidator(max_value=len(dishes))
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
        pass
