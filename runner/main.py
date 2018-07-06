from Display import display_input
from threading import Thread
#   Elements and Indelement are imported, so their elements will be registered
import Elements
import Indelement
from Pckg.register import Register
from Pckg.storage import Storage
from info import Mutable
import sys
from Pckg.threadm import ThreadM
if sys.version_info[0] < 3:
    FileType = file
else:
    from io import TextIOWrapper as FileType


def main_fn():

    while 1:
        entries = display_input('mhc> ')
        entries = entries.split()
        chosen_elements = set()
        FileObj = None
        for entry in entries:
            if entry == 'fc':
                for el in Register.fullCheck:
                    chosen_elements.add(el)
                continue
            try:
                bias = Register.indelements[entry].bias()
                if callable(bias):
                    bias()
                elif type(bias) == FileType and bias.mode == 'w':
                    FileObj = bias
            except KeyError:
                pass

            try:
                chosen_elements.add(Register.elements[entry])
            except KeyError:
                continue
        if not len(chosen_elements):
            continue
        nodeIDs = display_input('Enter node id(s) by space:    ').split()

        output = Storage()

        threads = []

        for element in chosen_elements:

            for nodeID in nodeIDs:
                t = Thread(target=output.store, args=(nodeID, element,))
                # t.start()
                threads.append(t)
        ThreadM(threads, Mutable.__numberThread__).start()
        # for th in threads:
        #     th.join()
        # Data is received
        output.display(fileObj=FileObj)