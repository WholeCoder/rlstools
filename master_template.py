from person_rls_record import Person

class Template:
    def __init__(self):
        pass

    def generateTemplate(self):
        rows = Person().findAll()

        file_handle = open("index.py","w")

        headString='''
<html>
	<head>
		<title>Ruben's People</title>
	</head>
	<body>
		<table>
			<tbody>
				<tr>'''
        for key in rows[0].keys():
            headString += "<th>" + key + "</th>"

        headString += '				</tr>'
        headString += "<% for row in rows: %>"
        headString += '<tr>'
        for key in rows[0].keys():
            headString += "<td><%= str(row['"+key+"']) %></td>"
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
