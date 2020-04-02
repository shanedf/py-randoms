#!/usr/bin/env python3
"""Quick developer guides on type usage and type methods in Python.

Usage:

    basics.py <type>
    python3 basics.py <type>
"""
import sys, os

types = []

def getTypes():
    global types
    for filename in os.listdir("guides"):
        if filename.endswith(".py"):
            types.append(filename.split(".")[0])
    return types

def directory():
    print("Guides are available on the following types:")
    print(getTypes())

def main(arg):
    getTypes()
    if arg in types:
        mod = __import__("guides.%s" % (arg), fromlist=["show"])
        help(mod)
    else:
        print("Module {} not found!".format(arg))
        print("")
        print("Available modules: {}".format(types))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        directory()
    else:
        main(sys.argv[1])