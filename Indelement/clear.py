from Pckg.register import Register
from os import system


@Register.indelement
class Clear:
    name = 'cl'
    detail = 'clear'

    @staticmethod
    def bias():
        """
        @owner      :   erencanyilmaz
        @contact    :   erencan.yilmaz@kcctech.com
        """
        system('clear')
        return