MHC is a platform where user can create own command prompt to get data from cell towers.
Even though basic structure is in python, other programing languages are supported as well

MHC consists of two primary components:
    1) Elements
    2) Indelements
Both of these classes have to follow mhc structure.

#   1) Elements

Elements are used to define what commands need to be run to collect data from cell tower and what to do with that.
convert_output must return output to display and summary in strings. Summary might be left empty string if not needed.

convert_output is performed after data is received.
        :param rawOutput:   data from cell tower -- string
        :param nodeid   :   Cell Tower ID -- string
        :return         :   (output_to_display, summary) -- (string, string)

Register.element wrapper is used to register element into mhc system. It checks if class structure is correct, and
performs simulation by sending fake input. Time out is set to 1.5 seconds.

```python
from Pckg.register import Register


@Register.element
class ElementName:
    name = One-word Key Name to display in menu
    detail = What this element is used for
    commands = [command_0, command_1, command_2, ...]
    fullCheck = Boolean    # Is this part Of Full Check?

    @staticmethod
    def convert_output(rawOutput, nodeid):
        """
        @owner      :
        @contact    :
        """
        #   rawOutput is output of commands
        #   nodeid is Cell Tower ID
        #   manipulate, edit raw output to display and make summary
        #   return output_to_display and summary in string
        return output_to_display, summary
```


#   2) Inelements

Indelements are used to give directions such as creating log file, setting number of thread at a time.
They are also used to for general operations.

Register.indelement wrapper is used to register indelement into mhc system. It checks if class structure is correct.

bias is performed right away. Check Indelement folder for more example
        :return         :   function which will be executed

```python
from Pckg.register import Register


@Register.indelement
class IndElementName:
    name = One-word Key Name to display in menu
    detail = What this element is used for

    @staticmethod
    def bias():
        """
        @owner      :
        @contact    :
        """
        # do stuff
        return function
```


#   Some helper modules

```python
#   To add color
from Display.display import Color

#   To create nice table to display
from Pckg.createTable import ctable

#   To read table for commands ending with c
from Pckg.tablec import TableC

#   To locate mhc and path where script is run
from Pckg.path import Path
```