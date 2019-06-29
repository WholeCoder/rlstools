from person_rls_record import Person

rows = Person().findAll()

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

for row in rows:
    headString += '<tr>'
    for key in rows[0].keys():
        headString += "<td>" + str(row[key]) + "</td>"
    headString += '</tr>'
headString += '''
                        </tbody>
		</table>
	</body>
</html>
'''

print(headString)
