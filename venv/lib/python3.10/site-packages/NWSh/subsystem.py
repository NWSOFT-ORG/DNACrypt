import sys

from prompt_toolkit import HTML, print_formatted_text, PromptSession
from prompt_toolkit.output.color_depth import ColorDepth as Depth
from prompt_toolkit.styles import Style

from NWSh.printing import print_error
from NWSh.settings import Settings

DEFAULT_PREFERENCES = {
    "name"       : "(none)",
    "version"    : "0.1",
    "description":  # language=HTML
    "<i>No description</i>",
    "author"     : "Anonymous",
    "license"    : "MIT",
}


class Subsystem:
    commands = {
        "exit": lambda: sys.exit(0)
    }

    def __init__(self, name: str = "(none)", preferences=None):
        if preferences is None:
            preferences = {}
        self.preferences = DEFAULT_PREFERENCES | preferences
        self.name = name
        self.prompt = f"{name}> "
        self.session = PromptSession()
        self.settings = Settings()
        self.style = None
        self.number = 0
        self.get_style()

        # language=HTML
        self.ctrl_c_msg = HTML(
            f"<subsystem_name>{self.name}</subsystem_name>: Press <b>Ctrl</b>+<b>D</b> (EOF) to exit."
        )

        self.print_welcome()

    def print_welcome(self):
        # language=HTML
        print_formatted_text(
            HTML(
                f"""\
<title><b>{self.preferences["name"]}</b> version {self.preferences["version"]}
By {self.preferences["author"]}, under the {self.preferences["license"]} license
</title>\
<description>\
{self.preferences["description"]}
</description>\
            """,
            ),
            style=self.style,
        )

    def get_style(self):
        self.style = Style.from_dict(
            self.settings.get("styles")
            [self.settings.get("using")]
        )

    def command_not_found(self):
        print_error(self.name, "Command not found")

    def execute_command(self, name):
        try:
            command_function = self.commands[name]
        except KeyError:
            command_function = self.command_not_found
        command_function()

    def ask_command(self):
        self.prompt = HTML(
            # language=HTML
            f"<subsystem_name>({self.name})</subsystem_name> "
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


