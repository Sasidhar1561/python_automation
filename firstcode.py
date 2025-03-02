#!/usr/bin/python3

import os
PATH = "/tmp/python3"

if os.path.isdir(PATH):
    print("It is a directory")
elif os.path.isfile(PATH):
    print("It is a textfile")
else:
    print("There is no file or directory with the PATH")

