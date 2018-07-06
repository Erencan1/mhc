from Pckg.register import Register


@Register.element
class CVSS:
    name = 'cvss'
    detail = 'CROSSDU, VOLTE SCHEDULING, SYSCONSTANT, SW STATUS'
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
