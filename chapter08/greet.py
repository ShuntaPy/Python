def greet_to(name):
    print("Hello {}-san".format(name))

def make_greet(name):
    greet="Hello {}-san".format(name)
    return greet

from greet import greet_to
greet_to("Tanaka")

import greet as gt
gt.greet_to("Tanaka")
