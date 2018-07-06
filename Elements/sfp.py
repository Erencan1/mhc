from Pckg.register import Register


@Register.element
class SFP:
    name = 'sfp'
    detail = 'SFP, TN SFP STATUS (uses cache)'
    commands = []
    fullCheck = True
    cache = {}

    @classmethod
    def use_cache(cls, nodeid):
        return cls.cache[nodeid]

    @staticmethod
    def convert_output(rawOutput, nodeid):
        """
        @owner      :
        @contact    :
        """
        # process rawOutput
        # return output_to_display, summary
        return '', ''
