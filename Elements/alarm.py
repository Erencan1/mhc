from Pckg.register import Register


@Register.element
class Alarm:
    name = 'alt'
    detail = 'alarm status'
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