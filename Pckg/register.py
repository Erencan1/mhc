"""

    Register Elements and Indelements. If structure is different, raise an error.

"""
from Pckg.timeOut import TimeProcess


class Register:

    elements = {}
    indelements = {}
    lgst = 0
    fullCheck = set()
    timeout = 1.5

    @staticmethod
    def _attr_check(the_class, attr, conditionF):
        if attr not in the_class.__dict__:
            raise AttributeError('%s must have "%s" attribute' % (the_class, attr))
        error = conditionF(the_class.__dict__[attr])
        if error:
            error = '%s.%s must be: %s' % (the_class, attr, error)
            raise ValueError(error)

    @staticmethod
    def _simulate_convert_output(the_class, attr, *args):
        try:
            the_function = getattr(the_class, attr)
            the_return = TimeProcess(Register.timeout, the_function, *args).get_result()
            # the_return = the_function(*args)
            assert type(the_return) == tuple and len(the_return) == 2 \
                   and all(type(the_r) == str for the_r in the_return), 'must return (string_output, string_summary)'
        except Exception as e:
            raise ValueError('%s.%s(rawOutput, nodeid): %s' % (the_class, attr, e))

    @classmethod
    def element(cls, the_class):
        cls._attr_check(the_class, 'name',
                        lambda attrV: 'one word' if type(attrV) != str or len(attrV.split()) != 1 else None)
        cls._attr_check(the_class, 'detail',
                        lambda attrV: 'non-empty string' if type(attrV) != str or not len(attrV) else None)
        cls._attr_check(the_class, 'commands',
                        lambda attrV: 'non-empty list' if type(attrV) != list or not len(attrV) else None)
        cls._attr_check(the_class, 'convert_output', lambda attrV: 'staticmethod' if type(attrV) != staticmethod or
                                                                                     cls._simulate_convert_output(
                                                                                         the_class,
                                                                                         'convert_output',
                                                                                         '\nrawOutput\n',
                                                                                         'nodeid'
                                                                                     ) else None)

        cls._attr_check(the_class, 'fullCheck', lambda attrV: 'Boolean' if type(attrV) != bool else None)
        if the_class.fullCheck:
            cls.fullCheck.add(the_class)

        cls.elements[the_class.name] = the_class
        if len(the_class.name) > cls.lgst:
            cls.lgst = len(the_class.name)

    @classmethod
    def indelement(cls, the_class):
        cls._attr_check(the_class, 'name',
                        lambda attrV: 'one word' if type(attrV) != str or len(attrV.split()) != 1 else None)
        cls._attr_check(the_class, 'bias', lambda attrV: 'staticmethod' if type(attrV) != staticmethod else None)
        cls.indelements[the_class.name] = the_class
        if len(the_class.name) > cls.lgst:
            cls.lgst = len(the_class.name)


class RegisterMeta(type):
    def __call__(self, name, type='elements'):
        return getattr(self, type)[name]


Register = RegisterMeta(Register.__name__, Register.__bases__, dict(Register.__dict__))