from Pckg.register import Register
from Display import display_input
import os


@Register.indelement
class Log:

    name = 'log'
    detail = 'Create Log File'

    @staticmethod
    def bias():
        """
        @owner      :   erencanyilmaz
        @contact    :   
        """
        # os.getcwd()
        fileName = '%s.txt' % display_input('Log File Name:    ')
        while os.path.exists(fileName):
            fileName = '%s.txt' % display_input('%s exists!, Enter Log File Name:    ' % fileName)
        return open(fileName, 'w')
