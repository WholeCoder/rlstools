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

