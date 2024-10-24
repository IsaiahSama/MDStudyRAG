try:
    from tools.utils.base_menu import BaseMenu
    from tools.utils.cli_menu import CliMenu
except ImportError:
    from .base_menu import BaseMenu
    from .cli_menu import CliMenu