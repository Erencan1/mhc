from Pckg.register import Register
from .display import Dprint, Color


def display_node_name(nodeName, fileObj=None):
    space = '      '
    at = '%s%s' % (space, '@' * (len(nodeName) + 4))
    nodeName = '%s@ %s @' % (space, nodeName)
    Dprint(at, Color.asda, fileObj=fileObj)
    Dprint(nodeName, Color.blue, fileObj=fileObj)
    Dprint(at, Color.asda, fileObj=fileObj)


def display_output(output, fileObj=None):
    for elementName, element in Register.elements.items():
        try:
            nodes_output = output[element.name]
        except KeyError:
            continue
        Dprint(element.detail, Color.blue, fileObj=fileObj)
        Dprint('\n', fileObj=fileObj)
        for node_id, node_output in nodes_output.items():
            display_node_name(node_id, fileObj=fileObj)
            Dprint(node_output, fileObj=fileObj)
        Dprint('\n', fileObj=fileObj)
