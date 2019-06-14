#!/usr/bin/python
import sys

print("Inside of write__model_template.py. directory == "+sys.argv[0])
print("app direcotry name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

new_model = open(sys.argv[1]+"/"+sys.argv[2]+".py",'w')

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


