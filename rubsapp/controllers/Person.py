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
    def get_form():
        print("dummy value")

    @staticmethod
    def post():
        print("dummy value")

    def put(self):
        pass

    def get(self):
        pass

