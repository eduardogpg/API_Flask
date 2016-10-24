from flask import g
from flask import abort
from flask import Flask
from flask import jsonify
from flask import make_response

import json
from bson import json_util

import models
from models import Course

app = Flask(__name__)

@app.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response

@app.errorhandler(404)
def not_found(error):
	return make_response( jsonify({'error': 'Not found'} ), 404)

@app.route('/codigo/api/v1.0/courses/', methods=['GET'])
def get_tasks():
	courses = Course.select()
	courses = [ course.to_json() for course in courses]
	return jsonify( generate_response( data = courses ) )

@app.route('/codigo/api/v1.0/courses/<int:course_id>', methods=['GET'])
def get_task(course_id):
	try:
		course = Course.get(Course.id == course_id)
	except Course.DoesNotExist:
		abort(404)
	return jsonify( generate_response(course.to_json() ) )

def generate_response(data = None):
	return { 'data': data }


if __name__ == '__main__':
	models.initialize()
	app.run(port=8000, debug=True)


