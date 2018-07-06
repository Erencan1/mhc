from Pckg.register import Register
from .display import Color, Dprint


def display_menu():
    try:
        Dprint(display_menu.menu)
        return
    except AttributeError:
        pass
    menu = [
        Color.asda,
        '\n   %-*s :     %s' % (Register.lgst, 'fc', 'Full Health Check'),
    ]

    for elementName, element in Register.elements.items():
        if hasattr(element, 'cache'):
            elementdetail = '%s (uses cache)' % element.detail
        else:
            elementdetail = element.detail
        menu.append(
            '   %-*s :     %s' % (Register.lgst, element.name, elementdetail)
        )
    if len(Register.indelements):
        menu.append('\n')
    for elementName, element in Register.indelements.items():
        menu.append(
            '   %-*s :     %s' % (Register.lgst, element.name, element.detail)
        )
    menu.append('\n')
    display_menu.menu = '\n'.join(menu)
    Dprint(display_menu.menu)



