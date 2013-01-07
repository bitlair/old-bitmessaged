import re, random
from boblight import Boblight
import time
from ctypes import *

def test():
    print("Bitlicht module test complete")
    return

def flash():
    bob = Boblight()
    bob.bob_loadLibBoblight("libboblight.so","linux")
    ret = bob.bob_connect("192.168.88.10", 19333)
    bob.bob_set_priority(1)
    aan = (c_int * 3)()
    aan[0] = 255
    aan[1] = 255
    aan[2] = 255
    uit = (c_int * 3)()
    uit[0] = 0
    uit[1] = 0
    uit[2] = 0
    for x in range(1,3):
        bob.bob_set_static_color(byref(aan))
        time.sleep(.5)
        bob.bob_set_static_color(byref(uit))
        time.sleep(.5)
    bob.bob_destroy()
