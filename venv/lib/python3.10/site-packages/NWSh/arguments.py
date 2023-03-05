from typing import Dict, Union

from prompt_toolkit import HTML

from NWSh.printing import print_error
from NWSh.subsystem import Subsystem


class Arguments(Subsystem):
    def __init__(self, name: str = "(none)", preferences=None):
        super().__init__(name, preferences)
        self.arguments: Dict[str, Union[str, int, float]] = {}

    def print_welcome(self):
        return  # Do not print welcome message, as this is not a "normal" subsystem

    def ask_argument(self, argument_name: str, argument_description: str, argument_type: str = "str"):
        # language=HTML
        self.prompt = HTML(
            f"<subsystem_name>{self.name}</subsystem_name>"
            f"<number>({argument_name})</number>"
            f"<prompt>></prompt> "
        )
        self.arguments[argument_name] = self.session.prompt(self.prompt, rprompt=argument_description, style=self.style)

        if argument_type == "int":
            try:
                self.arguments[argument_name] = int(self.arguments[argument_name])
            except ValueError:
                print_error(self.name, f"Argument {argument_name} must be an integer")
                self.ask_argument(argument_name, argument_description, argument_type)
        elif argument_type == "float":
            try:
                self.arguments[argument_name] = float(self.arguments[argument_name])
            except ValueError:
                print_error(self.name, f"Argument {argument_name} must be a float")
                self.ask_argument(argument_name, argument_description, argument_type)

    def get_argument(self, argument_name: str):
        try:
            return self.arguments[argument_name]
        except KeyError:
            print_error(self.name, f"Argument {argument_name} not found")
            return None
