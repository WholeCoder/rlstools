import sys

sys.path.append('../..')

from rubsapp.models.Office import Office

class OfficeController:
    @staticmethod
    def index():
        print("Running template_Output")

        OfficeController.rows = Office().findAll()
        print("rows == "+str(OfficeController.rows))
        OfficeController.dummyText = "<h1>Dummy Header</h1>"

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

OfficeController.index()
currString = ''

currString += ''
currString += '<html>'
currString += '	<head>'
currString += '		<title>Office List</title>'
currString += '	</head>'
currString += '	<body>'
currString += '		'
currString +=  OfficeController.dummyText 
currString += ''
currString += '		<table>'
currString += '			<tbody>'
currString += '				<tr><th>address</th><th>city</th><th>zip_code</th>				</tr>'
for row in OfficeController.rows: 
   currString += '<tr><td>'
   currString +=  str(row["address"]) 
   currString += '</td><td>'
   currString +=  str(row["city"]) 
   currString += '</td><td>'
   currString +=  str(row["zip_code"]) 
   currString += '</td></tr>'
currString += '  '
currString += '                        </tbody>'
currString += '		</table>'
currString += '	</body>'
currString += '</html>'
currString += ''
