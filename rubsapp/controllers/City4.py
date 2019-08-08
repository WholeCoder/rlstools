import sys

sys.path.append('../..')

from rubsapp.models.City4 import City4

class City4Controller:
    @staticmethod
    def index():
        print("Running template_Output")

        City4Controller.rows = City4().findAll()
        print("rows == "+str(City4Controller.rows))

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

