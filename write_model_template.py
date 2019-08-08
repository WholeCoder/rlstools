#!/usr/bin/python3
import sys

print("Inside of write__model_template.py. directory == "+sys.argv[0])
print("app direcotry name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

classHeader = "import sys\n\n"
classHeader += "sys.path.append('../..')\n\n"
classHeader += "from base_rls_record import BaseRlsRecord\n\n"
classHeader += "class "+sys.argv[2]+"(BaseRlsRecord):\n"
with open(sys.argv[1]+"/"+sys.argv[2]+".py", 'w') as new_model:
    new_model.write(classHeader)
    new_model.write("   pass\n")
    new_model.close()
