#!/usr/bin/python3
import re
import sys
import os

class TemplateParser:
    def __init__(self,template_file,table):
        print("template parser running---------------------->")
        file_handle = open(template_file,"r")
        print("template file == " + template_file)
        print("curret working directory == "+sys.argv[0])

        file_contents = file_handle.read()
        self.currString = ""
        debug = False

        if ".get" in table:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            print("dir_path == " + dir_path)

            lines = file_handle.readlines()
            for l in lines:
                self.currString += l
            file_handle.close()
        
            print("file contents is == " + self.currString)
            file_handle = open("template_output.py","w")
            file_handle.write(file_contents)
            file_handle.close()    
            
            return

        self.currString += "from rubsapp.models."+table+" import "+table+"\n\n"
        self.currString += "print(\"Running template_Output\")\n\n"

        self.currString += "rows = "+table+"().findAll()\n"
        self.currString += "print(\"rows == \"+str(rows))\n\n"
        
        self.currString += "currString = \"\"\n"

        results = re.split("<%", file_contents)
        for res in results:
            #currString += res)
            if res.startswith('='):
                command_with_text = res[1:].strip().split("%>")
                command = command_with_text[0]
                self.currString += "     currString +="+command+'\n'
                self.currString += '     currString +="'+"".join(command_with_text[1].split())+'"\n'
                if debug:
                    print("4")
            elif res.startswith(' for'):
                self.currString += res.split("%>")[0].strip()+"\n"
                self.currString += '     currString +="'+"".join(res.split("%>")[1].split())+'"\n'
                if debug:
                    print("3")
            else:
                if res.startswith("<html>"):
                    if debug:
                        print("2")
                    self.currString += '     currString +="'+"".join(res.split())+'"\n'
                else:
                    if debug:
                        print("1")
                    re2 = res.split("%>")
                    #print(re2)
                    #print(re2[0])
                    if len(re2) == 2:
                        self.currString += 'currString +="'+"".join(re2[1].split())+'"\n'
                    else:
                        self.currString += 'currString +="'+"".join(re2[0].split())+'"\n'
        self.currString += "\n\n\n"
        file_handle.close()
        file_handle = open("template_output.py","w")
        file_handle.write(self.currString)
        file_handle.close()
