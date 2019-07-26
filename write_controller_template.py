#!/usr/bin/python3
import sys

print("Inside of write__controller_template.py. directory == "+sys.argv[0])
print("app direcotry name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

new_controller = open(sys.argv[1]+"/"+sys.argv[2]+".py",'w')

classHeader = "import sys\n\n" 
classHeader += "sys.path.append('../..')\n\n" 
classHeader += "from rubsapp.models."+sys.argv[2]+" import "+sys.argv[2]+"\n\n" 

classHeader += "class "+sys.argv[2] + "Controller:\n" 
new_controller.write(classHeader)

count = 3

defHeader =  "    @staticmethod\n"
defHeader +=  "    def index():\n"
defHeader += "        print(\"Running template_Output\")\n\n"

defHeader += "        PersonController.rows = "+sys.argv[2]+"().findAll()\n"
defHeader += "        print(\"rows == \"+str("+sys.argv[2]+"Controller.rows))\n\n"

new_controller.write(defHeader)

defHeader = "    @staticmethod\n"
defHeader += "    def post():\n"
new_controller.write(defHeader)
passText =  "        print('dummy test')\n\n"
new_controller.write(passText)
 
defHeader = "    @staticmethod\n"
defHeader += "    def put():\n"
new_controller.write(defHeader)
new_controller.write(passText)

defHeader +="   @staticmethod"
defHeader += "    def get():\n"
new_controller.write(defHeader)
new_controller.write(passText)
 

new_controller.close()
