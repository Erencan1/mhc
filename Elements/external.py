from Pckg.register import Register


@Register.element
class ExternalAlarm:
    name = 'ext'
    detail = 'External Alarm'
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
