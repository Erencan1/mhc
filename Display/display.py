import re
import sys


remove_color_re = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
remove_color = lambda string: remove_color_re.sub('', string)


class Color:
    blue = '\033[94m'
    asda = '\033[92m'
    white = '\033[0m'
    green = '\033[0;32m'
    yellow = '\033[1;33m'
    red = '\033[0;31m'


Dprint = None
d2 = """
def Dprint(string, clr=Color.white, fileObj=None):
    print clr + string + Color.white
    if fileObj:
        fileObj.write(remove_color(string))
        fileObj.write('\\n')
"""
d3 = """
def Dprint(string, clr=Color.white, fileObj=None):
    print(clr + string + Color.white)
    if fileObj:
        fileObj.write(remove_color(string))
        fileObj.write('\\n')
"""

if sys.version_info[0] < 3:
    exec(d2)
else:
    exec(d3)
