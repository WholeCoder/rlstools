from rubsapp.models.Person import Person

print("Running template_Output")

rows = Person().findAll()
print("rows == "+str(rows))

currString = ''

currString += ''
currString += '<html>'
currString += '	<head>'
currString += '		<title>Person List</title>'
currString += '	</head>'
currString += '	<body>'
currString += '		<table>'
currString += '			<tbody>'
currString += '				<tr><th>first_name</th><th>last_name</th><th>ssn</th>				</tr>'
for row in rows: 
   currString += '<tr><td>'
   currString +=  str(row["first_name"]) 
   currString += '</td><td>'
   currString +=  str(row["last_name"]) 
   currString += '</td><td>'
   currString +=  str(row["ssn"]) 
   currString += '</td></tr>'
currString += '  '
currString += '                        </tbody>'
currString += '		</table>'
currString += '	</body>'
currString += '</html>'
currString += ''
