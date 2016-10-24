from flask import g
from flask import abort
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

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
	return jsonify( generate_response(404, error = 'Not found' ) )

@app.errorhandler(400)
def not_found(error):
	return jsonify( generate_response(400, error = 'Bad Request' ) )

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
	return jsonify( generate_response(data = course.to_json() ) )

@app.route('/codigo/api/v1.0/courses/', methods=['POST'])
def post_task():
	print "Entro aqui"
	if not request.json:
		abort(400)
	course = Course.new(title = request.json.get('title', ""),
									slug = request.json.get('slug', ""),
									description = request.json.get('description', "") )

	return jsonify( generate_response(data = course.to_json() ) )	

def generate_response(status = 200 , data = None, error = None):
	return { 'status': status, 'data': data, 'error': error}


if __name__ == '__main__':
	models.initialize()
	app.run(port=8000, debug=True)


