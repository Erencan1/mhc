from threading import Thread


class TimeProcess:
    """
        Raise time out error if thread should not complete in given timeout.
    """

    def __init__(self, timeout, fun, *args):
        """
        :param timeout: in second
        :param fun:     function
        :param args:    function arguments
        """
        self.fun = fun
        self.args = args
        self.timeout = timeout
        self.error = None

    def _handle(self):
        try:
            self.result = self.fun(*self.args)
        except Exception as e:
            self.error = e

    def get_result(self):
        t = Thread(target=self._handle)
        t.setDaemon(True)
        t.start()
        t.join(self.timeout)
        try:
            if self.error:
                raise self.error
            return self.result
        except AttributeError:
            raise TimeoutError('TimeOut Error (%s second)' % self.timeout)

