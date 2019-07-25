import sys

sys.path.append('../..')

from rubsapp.models.Person import Person

class PersonController:
    @staticmethod
    def index():
        print("Running template_Output")

        PersonController.rows = Person().findAll()
        print("rows == "+str(PersonController.rows))

    def post(self):
        pass

    def put(self):
        pass

    def get(self):
        pass

