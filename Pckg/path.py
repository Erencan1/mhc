import os


class Path:

    folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    execute = os.popen('pwd').read().strip()

    @classmethod
    def locate(cls, *args):
        p = os.path.join(cls.folder, *args)
        if not os.path.exists(p):
            raise FileExistsError('Not found: %s' % p)
        return p

    @classmethod
    def get_execute(cls, *args):
        return os.path.join(cls.execute, *args)
