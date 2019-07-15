#!/usr/bin/python3
from person_rls_record import Person
from sqlite_adapter import SqliteDatabaseAdapter
import sys # sys.argv[]

class Template:
    def __init__(self):
        pass

    def generateTemplate(self):

        parameter_list = []
        count = 3
        while count < len(sys.argv):
            parameter_list.append(sys.argv[count].split(":")[0])
            count += 1
        print("parameter_list == " + str(parameter_list))
        file_handle = open(sys.argv[1]+"/"+sys.argv[2]+".pyht",'w')
        headString='''
<html>
	<head>
		<title>'''
        headString += sys.argv[2] + " List"
        headString+='''</title>
	</head>
	<body>
		<table>
			<tbody>
				<tr>'''

        print("second parameter_list"+str(parameter_list))
        count = 0
        while count < len(parameter_list):
            headString += "<th>" + parameter_list[count] + "</th>"
            count += 1

        headString += '				</tr>'
        headString += "<% for row in rows: %>"
        headString += '<tr>'
        count = 0
        while count < len(parameter_list):
            headString += "<td><%= str(row['"+parameter_list[count]+"']) %></td>"
            count += 1
        headString += '</tr>'
        headString += "<% end-for %>"
        headString += '''
                        </tbody>
		</table>
	</body>
</html>
'''

        print(headString)
        file_handle.write(headString)
        file_handle.close()
#########

    def generateFormTemplate(self):

        parameter_list = []
        count = 3
        while count < len(sys.argv):
            parameter_list.append(sys.argv[count].split(":")[0])
            count += 1
        print("parameter_list == " + str(parameter_list))
        file_handle = open(sys.argv[1]+"/"+sys.argv[2]+".get.pyht",'w')
        headString='''
<html>
	<head>
		<title>'''
        headString += sys.argv[2] + " Form"
        headString+='''</title>
	</head>
	<body>
		<table>
			<tbody>'''
        headString += "<form action=\"/"+sys.argv[2]+"\" method=\"post\">"
        print("second parameter_list"+str(parameter_list))
        count = 0
        while count < len(parameter_list):
            headString += "<tr>"
            headString += "<td>" + parameter_list[count] + "</td>"
            headString += "<td><input type=\"text\" name=\""+parameter_list[count]+"\"/></td>"
            headString += '</tr>'
            count += 1
        headString += "<tr><td colspan=2 ><button type=\"submit\">Send your message</button></td></tr>"
        headString += "</form></tbody></table></body></html>"
        
        print(headString)
        file_handle.write(headString)
        file_handle.close()

Template().generateTemplate()
Template().generateFormTemplate()

