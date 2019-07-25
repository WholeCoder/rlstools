import sys

sys.path.append('../..')

from rubsapp.controllers.Person import PersonController

from rubsapp.models.Person import Person

PersonController.index()
rows = PersonController.rows

currString = ''

currString += ''
currString += '<html>'
currString += '	<head>'
currString += '		<title>Person List</title>'
currString += '	</head>'
currString += '	<body>'
currString += '		<table>'
currString += '			<tbody>'
currString += '				<tr><th>first_name</th><th>last_name</th>				</tr>'
for row in rows: 
   currString += '<tr><td>'
   currString +=  str(row["first_name"]) 
   currString += '</td><td>'
   currString +=  str(row["last_name"]) 
   currString += '</td></tr>'
currString += '  '
currString += '                        </tbody>'
currString += '		</table>'
currString += '	</body>'
currString += '</html>'
currString += ''
