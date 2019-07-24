import sys

sys.path.append('../..')

from rubsapp.models.Person import Person

class PersonController:
	def index(self):
		print("Running template_Output")

		rows = Person().findAll()
		print("rows == "+str(rows))


	def post(self):
		pass
	def put(self):
		pass
	def get(self):
		pass