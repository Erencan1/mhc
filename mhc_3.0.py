from Display import mhc_logo, display_menu
from info import __mhcPassword__
import getpass
import sys
from runner import main_fn


if __name__ == '__main__':

    if getpass.getpass() != __mhcPassword__:
        sys.exit()

    mhc_logo()
    display_menu()

    error = None
    try:
        main_fn()
    except Exception as e:
        error = e
    if error:
        raise error
