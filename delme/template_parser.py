import re

file_handle = open("template.ty","r")

file_contents = file_handle.read()

currString = ""

debug = False

table = "Person"
print("rows = "+table+"().findAll()")

results = re.split("<%", file_contents)
for res in results:
    #print(res)
    if res.startswith('='):
        command_with_text = res[1:].strip().split("%>")
        command = command_with_text[0]
        print("     print("+command+')')
        print('     print("'+"".join(command_with_text[1].split())+'"')
        if debug:
            print("4")
    elif res.startswith(' for'):
        print(res.split("%>")[0].strip())
        print('     print("'+"".join(res.split("%>")[1].split())+'")')
        if debug:
            print("3")
    else:
        if res.startswith("<html>"):
            if debug:
                print("2")
            print('     print("'+"".join(res.split())+'")')
        else:
            if debug:
                print("1")
            re2 = res.split("%>")
            #print(re2[0])
            print('print("'+"".join(re2[1].split())+'")')
    print("\n\n")
