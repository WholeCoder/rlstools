#!/usr/bin/python3
import sys

print("Inside of write__controller_template.py. directory == "+sys.argv[0])
print("app direcotry name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

new_controller = open(sys.argv[1]+"/"+sys.argv[2]+".py",'w')

classHeader = "import sys\n\n" 
classHeader += "sys.path.append('../..')\n\n" 
classHeader += "from rubsapp.models."+sys.argv[2]+" import "+sys.argv[2]+"\n\n" 

classHeader += "class "+sys.argv[2] + "Controller:" 
new_controller.write(classHeader)

count = 3

defHeader = "\n\tdef index(self):\n"
defHeader += "\t\tprint(\"Running template_Output\")\n\n"

defHeader += "\t\trows = "+sys.argv[2]+"().findAll()\n"
defHeader += "\t\tprint(\"rows == \"+str(rows))\n\n"

new_controller.write(defHeader)

defHeader = "\n\tdef post(self):"
new_controller.write(defHeader)
passText = "\n\t\tpass"
new_controller.write(passText)
 
defHeader = "\n\tdef put(self):"
new_controller.write(defHeader)
new_controller.write(passText)

defHeader = "\n\tdef get(self):"
new_controller.write(defHeader)
new_controller.write(passText)
 

new_controller.close()
