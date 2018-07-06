from Pckg.register import Register


@Register.element
class ROP:
    name = 'rop'
    detail = 'ROP RSSI STATUS'
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
