#!/usr/bin/python3
import sys

print("Inside of write__view_template.py. directory == "+sys.argv[0])
print("app directory name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

new_view = open(sys.argv[1]+"/"+sys.argv[2]+".html",'w')

count = 3
while count < len(sys.argv):
    new_view.write("<td>"+sys.argv[count]+"</td>")
    count += 1

new_view.close()
