from Pckg.register import Register
from .display import Dprint


def display_summary(summary, fileObj=None):
    for elementName, element in Register.elements.items():
        try:
            nodes_output = summary[element.name]
        except KeyError:
            continue
        Dprint('\n', fileObj=fileObj)
        Dprint(element.name, fileObj=fileObj)
        for nodeid in nodes_output:
            Dprint('%s: %s' % (nodeid, nodes_output[nodeid]), fileObj=fileObj)
        Dprint('\n', fileObj=fileObj)