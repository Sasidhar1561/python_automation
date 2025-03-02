#!/usr/bin/python3

import os

Userlist = ["alpha","beta","gamma"]

print("Adding users to the system")
print("*************************************************************************")

for user in Userlist:
    ec=os.system("id {}".format(user))
    if ec != 0:
        print()
        print("Adding user {} to the system".format(user))
        os.system("useradd {}".format(user))
        print("User successfully added")
    else:
        print("user already exist")
        print()

print("Adding group to the system")
print("*************************************************************************")

ec=os.system("grep science /etc/group")
if ec != 0:
    print()
    print("Adding science group to the system")
    os.system("groupadd science")
else:
    print()
    print("Group already exists")
    print()

print("Adding user to the science group")
print("*************************************************************************")


for user in Userlist:
    print()
    print("Adding {} user to the science group".format(user))
    os.system("usermod -G science {}".format(user))
    print("user {} successfully added to the science group".format(user))
    print()

print("Creating directory")
print("*************************************************************************")

if os.path.isdir("/opt/science"):
    print()
    print("Already dir exsist")
else:
    os.mkdir("/opt/science")
    print("successfully created dir")

print("Adding permission to the science dir")
print("*************************************************************************")

os.system("chown :science /opt/science")
os.system("chmod 770 /opt/science")
print()

