import sys

sys.path.append('../..')

from rubsapp.models.City2 import City2

class City2Controller:
    @staticmethod
    def index():
        print("Running template_Output")

        City2Controller.rows = City2().findAll()
        print("rows == "+str(City2Controller.rows))

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

