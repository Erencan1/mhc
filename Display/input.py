import sys
from .display import Color


if sys.version_info[0] < 3:
    inputF = eval('raw_input')
else:
    inputF = eval('input')


def display_input(st):
    return inputF(Color.red + st + Color.white)