import sys

sys.path.append('../..')

from rubsapp.models.City3 import City3

class City3Controller:
    @staticmethod
    def index():
        print("Running template_Output")

        City3Controller.rows = City3().findAll()
        print("rows == "+str(City3Controller.rows))

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

City3Controller.index()
currString = ''

currString += ''
currString += '<html>'
currString += '	<head>'
currString += '		<title>City3 List</title>'
currString += '	</head>'
currString += '	<body>'
currString += '		<table>'
currString += '			<tbody>'
currString += '				<tr><th>zipcode3</th><th>areacode3</th>				</tr>'
for row in City3Controller.rows: 
   currString += '<tr><td>'
   currString +=  str(row["zipcode3"]) 
   currString += '</td><td>'
   currString +=  str(row["areacode3"]) 
   currString += '</td></tr>'
currString += '  '
currString += '                        </tbody>'
currString += '		</table>'
currString += '	</body>'
currString += '</html>'
currString += ''
