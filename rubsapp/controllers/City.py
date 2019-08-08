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

