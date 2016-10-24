import datetime

from peewee import *

DATABASE = MySQLDatabase('API', host='localhost', user='root', passwd='')

class Course(Model):
	class Meta:
		database = DATABASE
		order_by = ('-created_at',)
		db_table = 'courses'

	title = CharField( unique = True, max_length = 250)
	slug = CharField( unique = True, max_length = 250)
	description = TextField()
	created_at = DateTimeField(default= datetime.datetime.now)

	def to_json(self):
		return {'id': self.id, 'title': self.title, 'slug': self.slug, 'description': self.description }

	@classmethod
	def new(cls, title, slug, description):
		try:
			return cls.create( title = title, slug = slug, description = description )
 		except IntegrityError:
 			return None

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Course], safe=True)
	DATABASE.close()

