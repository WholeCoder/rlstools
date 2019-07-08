#!/usr/bin/python3
from person_rls_record import Person
from sqlite_adapter import SqliteDatabaseAdapter
import sys # sys.argv[]

class Template:
    def __init__(self):
        pass

    def generateTemplate(self):
       
        count = 3
        while count < len(sys.argv):
            sys.argv[count] = sys.argv[count].split(":")[0]
            count += 1

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

        count = 3
        while count < len(sys.argv):
            headString += "<th>" + sys.argv[count] + "</th>"
            count += 1

        headString += '				</tr>'
        headString += "<% for row in rows: %>"
        headString += '<tr>'
        count = 3
        while count < len(sys.argv):
            headString += "<td><%= str(row['"+sys.argv[count]+"']) %></td>"
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

