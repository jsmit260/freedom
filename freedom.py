#! /usr/bin/python3
import os
import re

def isValid(x):
    ok = re.search("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",x)
    if ok:
        return True
    else:
        return False

i = input("Enter IP Addresses in the path to take each separated by a comma: ")
path  = i.split(",")
j = [i.strip() for i in path]
v = [isValid(i) for i in j]
if False in v:
    print("At least one invalid IP address given. Try again.")
    exit()
bs = 'ssh -R 9050 -J'
et = ''
c = [ et+' root@{}'.format(i) for i in j]
f=bs+' '.join(c)
print(f)
os.system(f)
