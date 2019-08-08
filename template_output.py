import sys

sys.path.append('../..')

from rubsapp.models.City import City

class CityController:
    @staticmethod
    def index():
        print("Running template_Output")

        CityController.rows = City().findAll()
        print("rows == "+str(CityController.rows))

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

CityController.index()
currString = ''

currString += ''
currString += '<html>'
currString += '	<head>'
currString += '		<title>City List</title>'
currString += '	</head>'
currString += '	<body>'
currString += '		<table>'
currString += '			<tbody>'
currString += '				<tr><th>zipcode</th><th>areacode</th>				</tr>'
for row in CityController.rows: 
   currString += '<tr><td>'
   currString +=  str(row["zipcode"]) 
   currString += '</td><td>'
   currString +=  str(row["areacode"]) 
   currString += '</td></tr>'
currString += '  '
currString += '                        </tbody>'
currString += '		</table>'
currString += '	</body>'
currString += '</html>'
currString += ''
