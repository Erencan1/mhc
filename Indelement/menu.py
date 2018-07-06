from Pckg.register import Register
from Display import display_menu


@Register.indelement
class Menu:
    name = 'l'
    detail = 'command list'

    @staticmethod
    def bias():
        """
        @owner      :   erencanyilmaz
        @contact    :   
        """
        return display_menu
