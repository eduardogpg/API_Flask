 #!/usr/bin/python
 # -*- coding: utf-8 -*-
 
import datetime

from peewee import *

DATABASE = MySQLDatabase('API', host='localhost', user='root', passwd='')

class Course(Model):
	title = CharField( unique = True, max_length = 250)
	slug = CharField( unique = True, max_length = 250)
	description = TextField()
	created_at = DateTimeField(default= datetime.datetime.now)

