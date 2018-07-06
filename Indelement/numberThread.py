from info import Mutable
from Pckg.register import Register
from Display import display_input


@Register.indelement
class NumberThread:

    name = 'nt'
    detail = 'Number of Thread'

    @staticmethod
    def bias():
        """
        @owner      :   erencanyilmaz
        @contact    :   
        """
        new__numberThread__ = display_input('cuurent number of thread running at a time: %s'
                                            '\nEnter new number:    ' % Mutable.__numberThread__).strip()
        try:
            new__numberThread__ = int(new__numberThread__)
            Mutable.__numberThread__ = new__numberThread__
        except:
            pass
        return
