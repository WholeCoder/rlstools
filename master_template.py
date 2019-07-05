from person_rls_record import Person
from database_adapter import DatabaseAdapter
import sys # sys.argv[]

class Template:
    def __init__(self):
        pass

    def generateTemplate(self):
        
        migration_number = DatabaseAdapter.getInstance().getNextDatabaseVersionNumber()
        file_handle = open(sys.argv[1]+"/"+migration_number+"__"+sys.argv[2]+".migration",'w')
        DatabaseAdapter.getInstance().createNewRecord("db_versions",{"version":migration_number})
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
        while count < len(sys.argv)
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

