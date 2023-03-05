from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.styles import Style

from NWSh.settings import Settings


def print_error(subsystem: str, error: str):
    settings = Settings()
    using_style = settings.get("styles")[settings.get("using")]
    style = Style.from_dict(using_style)
    # language=HTML
    print_formatted_text(
        HTML(f"<subsystem_name>{subsystem}</subsystem_name>|<error>ERR : {error}</error>"), style=style
    )


def print_warning(subsystem: str, warning: str):
    settings = Settings()
    using_style = settings.get("styles")[settings.get("using")]
    style = Style.from_dict(using_style)
    # language=HTML
    print_formatted_text(
        HTML(f"<subsystem_name>{subsystem}</subsystem_name>|<warning>WARN: {warning}</warning>"), style=style
    )


def print_info(subsystem: str, info: str):
    settings = Settings()
    using_style = settings.get("styles")[settings.get("using")]
    style = Style.from_dict(using_style)
    # language=HTML
    print_formatted_text(HTML(f"<subsystem_name>{subsystem}</subsystem_name>|<info>INFO: {info}</info>"), style=style)


def print_result(subsystem: str, result: str):
    settings = Settings()
    using_style = settings.get("styles")[settings.get("using")]
    style = Style.from_dict(using_style)
    # language=HTML
    print_formatted_text(
        HTML(f"<subsystem_name>{subsystem}</subsystem_name>|<result>=> {result}</result>"), style=style
    )
