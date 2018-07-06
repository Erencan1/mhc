# For advanced table reader, contact!
"""
    t = TableC()

    t.parse_with_key(input_1)
    t.parse_with_key(input_2)
    t.parse(input_3)

    all_tables = t.tables

    table = t.get(['key words exist in header'], multi=False)
    name_column_index, last_name_column_index = table.get_index(['name', 'last'])
    for row in table.rows:
        pass

"""


class TableC:
    class Table:
        def get_index(self, keys):
            sorted_array = list(h.lower() for h in self.header)
            for k, key in enumerate(keys):
                for i, a in enumerate(sorted_array):
                    if key.lower() in a:
                        sorted_array[i] = ''
                        keys[k] = i
            assert all(type(key) == int for key in keys), 'Keys (%s) does not match| %s' % (self.header, keys)
            return keys

    def __init__(self, breaker=(' ', ''), spliter=';', headerer=('=',)):
        self.breaker = breaker
        self.spliter = spliter
        self.headerer = headerer
        self.tables = []

    @staticmethod
    def strip(array):
        return list(a.strip() for a in array)

    def parse(self, rawoutput):
        toMemo = TableC.strip(rawoutput.split('\n'))
        i = 0
        while i < len(toMemo):
            line = toMemo[i]
            if i + 2 < len(toMemo) and line[:1] in self.headerer and toMemo[i + 2][:1] in self.headerer:
                table = TableC.Table()
                table.header = TableC.strip(toMemo[i + 1].split(self.spliter))  # header
                table.rows = []
                i = i + 3
                while i < len(toMemo):
                    line = toMemo[i]
                    if line[:1] in self.breaker:
                        break
                    row = TableC.strip(line.split(self.spliter))
                    if len(row) == len(table.header):
                        table.rows.append(row)
                    i += 1
                self.tables.append(table)
            i += 1

    def get(self, keys, multi=False, exact=False):
        findings = []
        for table in self.tables:
            if exact and all(key in table.header for key in keys):
                findings.append(table)
            elif not exact and all(any(key.lower() in h.lower() for h in table.header) for key in keys):
                findings.append(table)
        if not len(findings):
            raise Exception('Table not found for %s' % keys)
        if multi:
            return findings
        assert len(findings) == 1, 'Multiple table for %s' % keys
        return findings[0]

    def parse_with_key(self, rawoutput, key='MO', spliter=None, breaker=None):
        if not spliter:
            spliter = self.spliter
        if not breaker:
            breaker = self.breaker

        ylines = (yline for yline in rawoutput.split('\n'))
        for line in ylines:
            if line[:len(key)] == key:
                table = self.Table()
                table.header = self.strip(line.split(spliter))
                table.rows = []
                line = next(ylines)
                while 1:
                    row = self.strip(line.split(spliter))
                    if len(row) == len(table.header):
                        table.rows.append(row)
                    if line[:1] in breaker:
                        break
                    try:
                        line = next(ylines)
                    except StopIteration:
                        break
                self.tables.append(table)
