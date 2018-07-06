from Pckg.register import Register


@Register.element
class RAT:
    name = 'rat'
    detail = 'RET ANTENNA, TMA STATUS'
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
