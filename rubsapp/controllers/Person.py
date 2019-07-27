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

