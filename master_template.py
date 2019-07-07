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
		<title>Ruben's People</title>
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

Template().generateTemplate()

