from Pckg.register import Register
from Display import display_input, Dprint
from info import __mhcAuthor__


@Register.indelement
class Author:
    name = 'cnt'
    detail = 'Get contact info in case of error'

    @staticmethod
    def bias():
        """
        @owner      :   erencanyilmaz
        @contact    :   
        """
        text = '\n\nMHC Designer: %s\n\nChoose Section to grap element owner contact info\n\n%s\n\n> ' % (
            __mhcAuthor__, '\n'.join(Register.elements))
        section = '%s' % display_input(text)
        if section in Register.elements:

            return lambda: Dprint(Register.elements[section].convert_output.__doc__)
