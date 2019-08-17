#!/usr/bin/python3
import sys
import os

exists = os.path.isfile('../router.py')
print("-----------------------------working---------------")

if not exists:
    print("------------exists")
    with open("../router.py", "w") as router_file:
        router_file.write("router = {}\n")

print("-----------doesn't eist")
router_file = open("../router.py", "a+")
with open("../router.py", "a+") as router_file:
    print("--------writing router.py")
    router_file.write("\nrouter['"+sys.argv[2]+"'] = {}")
    router_file.write("\nrouter['"+sys.argv[2]+"']['get_form'] = '"+sys.argv[2]+".get.pyht'\n")# noqa
    router_file.write("router['"+sys.argv[2]+"']['index'] = '"+sys.argv[2]+".pyht'\n")# noqa

print("Inside of write__controller_template.py. directory == "+sys.argv[0])
print("app direcotry name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

new_controller = open(sys.argv[1]+"/"+sys.argv[2]+".py", 'w')
with open(sys.argv[1]+"/"+sys.argv[2]+".py", 'w') as new_controller:

    classHeader = "import sys\n\n"
    classHeader += "import html\n\n"
    classHeader += "sys.path.append('../..')\n\n"
    classHeader += "from models."+sys.argv[2]+" import "+sys.argv[2]+"\n\n" # noqa

    classHeader += "class "+sys.argv[2] + "Controller:\n"
    new_controller.write(classHeader)

    count = 3

    defHeader = "    @staticmethod\n"
    defHeader += "    def index():\n"
    defHeader += "        print(\"Running template_Output\")\n\n"

    defHeader += "        "+sys.argv[2]+"Controller.rows = "+sys.argv[2]+".findAll()\n"# noqa
    defHeader += "        print(\"rows == \"+str("+sys.argv[2]+"Controller.rows))\n\n"# noqa

    new_controller.write(defHeader)

    defHeader = "    @staticmethod\n"
    defHeader += "    def post():\n"
    new_controller.write(defHeader)
    passText = "        print('dummy test')\n\n"
    new_controller.write(passText)

    defHeader = "    @staticmethod\n"
    defHeader += "    def get_form():\n"
    new_controller.write(defHeader)
    passText = "        print('dummy test')\n\n"
    new_controller.write(passText)

    defHeader = "    @staticmethod\n"
    defHeader += "    def put():\n"
    new_controller.write(defHeader)
    new_controller.write(passText)

    defHeader = "    @staticmethod\n"
    defHeader += "    def get():\n"
    new_controller.write(defHeader)
    new_controller.write(passText)
