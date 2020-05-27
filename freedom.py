#! /usr/bin/python3
import os
import sys
i = input("Enter IP Addresses in the path to take each separated by a comma: ")
path  = i.split(",")
bs = 'ssh -R 9050 -J'
et = ''
c = [ et+' root@{}'.format(i) for i in path]
f=bs+' '.join(c)
os.system(f)
