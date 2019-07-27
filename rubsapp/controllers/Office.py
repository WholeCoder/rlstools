import sys

sys.path.append('../..')

from rubsapp.models.Office import Office

class OfficeController:
    @staticmethod
    def index():
        print("Running template_Output")

        OfficeController.rows = Office().findAll()
        print("rows == "+str(OfficeController.rows))

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

