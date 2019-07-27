import sys

sys.path.append('../..')

from rubsapp.models.Person import Person

class PersonController:
    @staticmethod
    def index():
        print("Running template_Output")

        PersonController.rows = Person().findAll()
        print("rows == "+str(PersonController.rows))

    @staticmethod
    def post():
        print('dummy test')

    @staticmethod
    def get_form():
        print('dummy test')

    @staticmethod
    def put():
        print('dummy test')

    @staticmethod
    def get():
        print('dummy test')

PersonController.index()
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
for row in PersonController.rows: 
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
