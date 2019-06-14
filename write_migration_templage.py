#!/usr/bin/python
import sys
import datetime

print("Inside of write__migration_template.py. directory == "+sys.argv[0])
print("app direcotry name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

now = datetime.datetime.now()


new_model = open(sys.argv[1]+"/"+now.year+"-"+now.month+"-"+now.day+"-"sys.argv[2]+".migration",'w')

classHeader = "class "+sys.argv[2] + "Model:" 
new_model.write(classHeader)

count = 3
while count < len(sys.argv):
    currentAttributeString = sys.argv[count]
    attributeName = currentAttributeString.split(":")[0]
    datatype = currentAttributeString.split(":")[1]

    defHeader = "\n\tdef "+attributeName+"(self,"+attributeName+"): # type = "+datatype
    new_model.write(defHeader)
    attributeBody = "\n\t\tself."+attributeName+"="+attributeName 
    new_model.write(attributeBody)
    count += 1

new_model.write("\n")


