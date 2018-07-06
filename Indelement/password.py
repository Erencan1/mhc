from Pckg.register import Register
from Pckg.path import Path


@Register.indelement
class Password:

    p = Path.locate('files', 'password.mos')

    name = 'pwd'
    detail = 'Add Username and Password for all elements (requires only once)'
    added = False

    @staticmethod
    def bias():
        """
        @owner      :   erencanyilmaz
        @contact    :   
        """
        pwd = Register('pwd', type='indelements')
        if pwd.added:
            return
        for eln, el in Register.elements.items():
            if any('lt' in cmd for cmd in el.commands):
                # if there is lt query, add pwd script
                el.commands = ['run %s' % pwd.p] + el.commands
        pwd.added = True
