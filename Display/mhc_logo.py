from info import __mhcVersion__, __releaseCyle__
from .display import Color, Dprint


def mhc_logo():
    Dprint('\n')
    Dprint('|\\    /|    |   |     ____', Color.blue)
    Dprint('| \\  / |    |---|    /')
    Dprint('|  \/  |    |   |    \\____  v%s %s' % (__mhcVersion__, __releaseCyle__), Color.blue)
    Dprint('\n')
