

import psutil


def find_process(process_name):
    if process_name in (p.name() for p in psutil.process_iter()):
        return True
    else:
        return False