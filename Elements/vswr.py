from Pckg.register import Register
from Pckg.path import Path


@Register.element
class VSWR:
    # when script in other programing language is preferred
    p = Path.locate('scripts', 'vswr.pl')
    mop = Path.get_execute('mo_vswr_$date_$nodename')

    name = 'vswr'
    detail = 'vswr status'
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

