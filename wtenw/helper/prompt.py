from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import Completer, Completion


class WelcomeValidator(Validator):
    def validate(self, document):
        if document.text not in ['v', 'g', 'a']:
            raise ValidationError(message='Please type a valid option')


class NumberValidator(Validator):
    def __init__(self, max_value: int):
        self.max_value = max_value
        super().__init__()

    def validate(self, document):
        try:
            a = int(document.text)
            if a not in range(1, self.max_value + 1):
                raise ValueError()
        except (TypeError, ValueError):
            raise ValidationError(message=f'Please type a number in range [1..{self.max_value}]')


class NotInStringListValidator(Validator):
    def __init__(self, string_list: list[str]):
        self.string_list = string_list
        super().__init__()

    def validate(self, document):
        if document.text in self.string_list:
            raise ValidationError(message=f'Please type a unique value. Name already known.')


class TestCompleter(Completer):
    def __init__(self, string_list: list[str]):
        self.string_list = string_list
        super().__init__()

    def get_completions(self, document, complete_event):
        for item in [i for i in self.string_list if i.startswith(document.text)]:
            yield Completion(item, start_position=0)
