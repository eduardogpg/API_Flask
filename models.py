import datetime

from peewee import *

DATABASE = MySQLDatabase('API', host='localhost', user='root', passwd='')

class Course(Model):
	class Meta:
		database = DATABASE
		#order_by = ('-created_at',)
		db_table = 'courses'

	title = CharField( unique = True, max_length = 250)
	slug = CharField( unique = True, max_length = 250)
	description = TextField()
	created_at = DateTimeField(default= datetime.datetime.now)
	released = BooleanField(default=True)

def initialize():
	"""Called when the program starts if not called as an imported module."""
	DATABASE.connect()
	DATABASE.create_tables([Course], safe=True)
	#insert()
	DATABASE.close()

def insert():
	first_course = Course(title='Curso Python3', slug = 'python3', description= 'Este es en nuevo curso de Python 3')
	first_course.save()