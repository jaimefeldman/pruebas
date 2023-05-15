# -*- coding: utf-8 -*-
"""
    animations.wheel
    ~~~~~~~~~~~~~~~~

    Una reuda clasica de linea de comandos para usando threads para 
    esperar algún proceso.

    :copyright: (c) 2023 by jaime a. feldman.
    :license: MIT, see LICENSE for more details.
"""

import itertools
import threading
import time
import sys

done = False
def wheel_animation():
    for c in itertools.cycle(['|','/','-','\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rdone!     ')

def start():
    t = threading.Thread(target=wheel_animation)
    t.start()

    # proceso que tarda algun tiempo.
    time.sleep(5)
    done = True

