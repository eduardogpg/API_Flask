 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import datetime
from peewee import *

DATABASE = MySQLDatabase('API', host='localhost', user='root', passwd='')

class Course(Model):
	class Meta:
		database = DATABASE
		order_by = ('id',)
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

class User(Model):
	class Meta:
		database = DATABASE
		order_by = ('id',)
		db_table = 'users'

	username = CharField(unique=True, max_length= 100)
	password = CharField(unique=True, max_length= 100)
	created_at = DateTimeField(default = datetime.datetime.now)

class Grand(Model):
	class Meta:
		database = DATABASE
		order_by = ('client_id',)
		
	user = ForeignKeyField(User, related_name='users')
	client_id = CharField(unique=True, max_length = 40, primary_key = True)
	client_secret = CharField(max_length = 55, unique = True, index = True, null = False)
	is_confidential = BooleanField()
	_redirect_uris = TextField()
	_default_scopes = TextField()

	@property
	def client_type(self):
		if self.is_confidential:
			return 'confidential'
		return 'public'

	@property
	def redirect_uris(self):
		if self._redirect_uris:
			return self._redirect_uris.split()
		return []

	@property
	def default_redirect_uri(self):
		return self.redirect_uris[0]

	@property
	def default_scopes(self):
		if self._default_scopes:
			return self._default_scopes.split()
		return []


def create_user():
	username = 'eduardo_gpg'
	password = 'password'
	if not User.select().where(User.username == username):
		User.create(username = username, password = password)

def create_course():
	title = 'Curso de Flask'
	slug = 'flask'
	description = 'Descripción del curso de Flask'
	if not Course.select().where(Course.slug == slug):
		Course.create(title = title, slug = slug, description = description )

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Course, User, Grand], safe=True)	
	create_course()
	create_user()
	DATABASE.close()

