"""
    ctable([['Name', 'Last Name'], ['name1', 'lastname1'], ['name2', 'lastname2']])
    or
    ctable([['name1', 'lastname1'], ['name2', 'lastname2']], pointHeader=['Name', 'Last Name'])
"""
from Display.display import remove_color


def update_distance(dist, array):
    for i, item in enumerate(array):
        try:
            d = dist[i]
        except KeyError:
            dist[i] = len(item)     # len(remove_color(item))
            continue
        if len(item) > d:
            dist[i] = len(item)     # len(remove_color(item))


def ctable(narray, pointHeader=True):
    distance = {}

    for array in narray:
        update_distance(distance, array)

    table = []
    f = 0
    if pointHeader:
        if type(pointHeader) == list:
            update_distance(distance, pointHeader)
        else:
            pointHeader = narray[0]
            f = 1
        row = []
        for i, item in enumerate(pointHeader):
            row.append('%-*s' % (distance[i], item))
        border = '=' * sum(v + 2 for k, v in distance.items())
        table.append(border)
        table.append('  '.join(row))
        table.append(border)

    for a in range(f, len(narray)):
        array = narray[a]
        row = []
        for i, item in enumerate(array):
            f = len(item) - len(remove_color(item))
            row.append('%-*s' % (distance[i]+f, item))
        table.append('  '.join(row))
    return '\n'.join(table)
