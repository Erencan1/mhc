from Pckg.register import Register


@Register.element
class Scanner:
    name = 'sl'
    detail = 'SCANNER, LINK BUDGET STATUS'
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
