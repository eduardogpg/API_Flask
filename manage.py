from flask import Flask
from flask import jsonify
from flask import abort
from flask import g
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

@app.route('/codigo/api/v1.0/courses/<int:course_id>', methods=['GET'])
def get_task(course_id):
	try:
		course = Course.get(Course.id == course_id)
	except Course.DoesNotExist:
		abort(404)
	return jsonify(  {'title': course.title }   )

if __name__ == '__main__':
	models.initialize()
	app.run(port=8000, debug=True)