Get method
curl -i http://localhost:8000/codigo/api/v1.0/courses/1

Post method
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"New Course", "slug": "new_course", "description": "This is a single description"}' http://localhost:8000/codigo/api/v1.0/courses/
