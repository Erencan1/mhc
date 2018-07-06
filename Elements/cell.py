from Pckg.register import Register
from Pckg.path import Path


@Register.element
class Cell:
    # when script in other programing language is preferred
    p = Path.locate('scripts', 'cell.pl')
    mop = Path.get_execute('mo_cell_$date_$nodename')

    name = 'cell'
    detail = 'CELL & TRAFFIC STATUS'
    commands = []
    fullCheck = True

    @staticmethod
    def convert_output(rawOutput, nodeid):
        """
        @owner      :
        @contact    :
        """
        # process rawOutput
        # return output_to_display, summary
        return '', ''
