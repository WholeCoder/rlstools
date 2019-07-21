currString = ''

from rubsapp.models.Office import Office

print("Running template_Output")

rows = Office().findAll()
print("rows == "+str(rows))

currString += ''
currString += '<html>'
currString += '	<head>'
currString += '		<title>Office List</title>'
currString += '	</head>'
currString += '	<body>'
currString += '		<table>'
currString += '			<tbody>'
currString += '				<tr><th>address</th><th>zip_code</th><th>city</th>				</tr>'
for row in rows: 
   currString += '<tr><td>'
   currString +=  str(row["address"]) 
   currString += '</td><td>'
   currString +=  str(row["zip_code"]) 
   currString += '</td><td>'
   currString +=  str(row["city"]) 
   currString += '</td></tr>'
currString += '  '
currString += '                        </tbody>'
currString += '		</table>'
currString += '	</body>'
currString += '</html>'
currString += ''
