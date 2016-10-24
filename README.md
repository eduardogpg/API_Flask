Get method
curl -i http://localhost:8000/codigo/api/v1.0/courses/1

Post method
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Nuevo curso", "slug": "nuevo_curso", "description": "Este es la descripción"}' http://localhost:8000/codigo/api/v1.0/courses/


Pust
curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"lalala del curso", "slug": "lalal", "description": "Este es la descripción"}' http://localhost:8000/codigo/api/v1.0/courses/1


curl -X DELETE http://localhost:8000/codigo/api/v1.0/courses/1