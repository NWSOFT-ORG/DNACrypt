import sys

from prompt_toolkit import HTML, print_formatted_text, PromptSession
from prompt_toolkit.output import ColorDepth as Depth

from NWSh.settings import Settings
from NWSh.subsystem import Subsystem


class System(Subsystem):
    commands = {}

    def __init__(self, name: str = "(none)", preferences=None):
        super().__init__(name, preferences)
        self.prompt = f"{name}> "
        self.session = PromptSession()
        self.settings = Settings()
        self.style = None
        self.number = 0
        self.get_style()

        # language=HTML
        self.ctrl_c_msg = HTML(
            f"<system_name>{self.name}</system_name>: Press <b>Ctrl</b>+<b>D</b> (EOF) to exit."
        )

    def ask_command(self):
        # language=HTML
        self.prompt = HTML(
            f"<system_name>{self.name}</system_name> "
            f"<number>[{self.number}]</number>"
            f"<prompt>></prompt> "
        )
        self.number += 1
        try:
            result = self.session.prompt(self.prompt, style=self.style, color_depth=Depth.TRUE_COLOR)
        except KeyboardInterrupt:
            print_formatted_text(self.ctrl_c_msg, style=self.style)
            return
        except EOFError:
            sys.exit(0)

        self.execute_command(result)
