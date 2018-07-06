"""
    Collect data per session and node, then store them
"""
from Pckg import SessionHouse
from Display import display_output, display_summary, Dprint


class Storage(dict):
    """
        {
            element.name : {
                                node_id: output/summary
                            }
        }
    """
    def __init__(self, **kwargs):
        try:
            super().__init__(**kwargs)
        except TypeError:
            # python 2
            pass
        self.summary = {}

    def store(self, nodeID, el):
        try:
            if len(el.commands):
                sh = SessionHouse()
                sh_output = sh(nodeID, el.commands)
            else:
                sh_output = ''
            output, summary = el.convert_output(sh_output, nodeID)
        except Exception as e:
            Dprint('!%s %s - %s' % (e, nodeID, el.name))
            return
        if len(output):
            self.insert(self, el.name, nodeID, output)
        if len(summary):
            self.insert(self.summary, el.name, nodeID, summary)

    @staticmethod
    def insert(the_dict, *args):
        assert len(args) > 1, KeyError('No value assignment')
        args = list(args)
        value = args.pop()
        lk = args.pop()
        for arg in args:
            try:
                the_dict = the_dict[arg]
            except KeyError:
                the_dict[arg] = {}
                the_dict = the_dict[arg]
        the_dict[lk] = value

    def display(self, fileObj=None):
        display_summary(self.summary, fileObj=fileObj)
        display_output(self, fileObj=fileObj)