from Pckg.register import Register
from Pckg.path import Path


@Register.element
class RSSI:
    # when script in other programing language is preferred
    p = Path.locate('scripts', 'rssi.pl')
    mop = Path.get_execute('mo_rssi_$date_$nodename')
    name = 'rssi'
    detail = 'REAL TIME RSSI'
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
