from Pckg.register import Register
import sys


@Register.indelement
class Quit:
    name = 'q'
    detail = 'quit'

    @staticmethod
    def bias():
        """
        @owner      :   erencanyilmaz
        @contact    :   
        """
        return sys.exit
