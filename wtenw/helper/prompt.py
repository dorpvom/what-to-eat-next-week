from prompt_toolkit.validation import Validator, ValidationError


class WelcomeValidator(Validator):
    def validate(self, document):
        if document.text not in ['v', 'g', 'a']:
            raise ValidationError(message='Please type a valid option')


class NumberValidator(Validator):
    def __init__(self, max_value):
        self.max_value = max_value
        super().__init__()

    def validate(self, document):
        try:
            a = int(document.text)
            if a not in range(1, self.max_value + 1):
                raise ValueError()
        except (TypeError, ValueError):
            raise ValidationError(message=f'Please type a number in range [1..{self.max_value}]')
