from flask import g
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

import models
from models import Course

app = Flask(__name__)
PORT = 8000
DEBUG = True
HOST = '0.0.0.0'

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
	return jsonify( generate_response(404, error = 'Not found' ) )

@app.errorhandler(400)
def not_found(error):
	return jsonify( generate_response(400, error = 'Bad Request' ) )

@app.errorhandler(422)
def not_found(error):
	return jsonify( generate_response(422, error = 'Unprocessable Entity' ) )

@app.route('/codigo/api/v1.0/courses/', methods=['GET'])
def get_courses():
	courses = Course.select()
	courses = [ course.to_json() for course in courses]
	return jsonify( generate_response( data = courses ) )

@app.route('/codigo/api/v1.0/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
	course = get_course(course_id)
	return jsonify( generate_response(data = course.to_json() ) )

@app.route('/codigo/api/v1.0/courses/', methods=['POST'])
def post_course():
	if not request.json:
		abort(400)
	course = Course.new(title = request.json.get('title', ""), slug = request.json.get('slug', ""),
											description = request.json.get('description', "") )
	if course is None:
		abort(422)
	return jsonify( generate_response(data = course.to_json() ) )	

@app.route('/codigo/api/v1.0/courses/<int:course_id>', methods=['PUT'])
def put_course(course_id):
	course = get_course(course_id)
	if not request.json:
		abort(400)

	course.title = request.json.get('title', course.title)
	course.slug = request.json.get('slug', course.slug)
	course.description = request.json.get('description', course.description)
	if course.save():
		return jsonify( generate_response(data = course.to_json() ) )	
	else:
		abort(422)

@app.route('/codigo/api/v1.0/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
	course = get_course(course_id)
	if course.delete_instance():
		return jsonify( generate_response(data = {} ) )
	else:
		abort(422)

def generate_response(status = 200 , data = None, error = None):
	return { 'status': status, 'data': data, 'error': error}

def get_course(course_id):
	try:
		return Course.get(Course.id == course_id)
	except Course.DoesNotExist:
		abort(404)

if __name__ == '__main__':
	models.initialize()
	app.run(port = PORT, debug = DEBUG, host = HOST)

