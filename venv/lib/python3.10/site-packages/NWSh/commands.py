from typing import Callable

from NWSh.printing import print_warning
from NWSh.subsystem import Subsystem
from NWSh.system import System


def register_command_system(system: System, command: str, func: Callable):
    if command in system.commands:
        print_warning(system.name, f"Command {command} already registered")
    system.commands[command] = func


def register_command_subsystem(subsystem: Subsystem, command: str, func: Callable):
    if command in subsystem.commands:
        print_warning(subsystem.name, f"Command {command} already registered")
    subsystem.commands[command] = func
