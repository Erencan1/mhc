import time


class ThreadM:
    """
    :arg
        threads :   threads in array
        n       :   number of threads running at a time
    """
    def __init__(self, threads, n):
        self.threads = list(reversed(threads))
        self.running_thread = [None] * n

    def start(self, sleep=1):
        while len(self.threads):
            for i, cell in enumerate(self.running_thread):
                if not (cell and cell.isAlive()):
                    try:
                        p = self.threads.pop()
                    except IndexError:
                        break
                    self.running_thread[i] = p
                    self.running_thread[i].start()
            time.sleep(sleep)
        for rest in self.running_thread:
            if rest:
                rest.join()
