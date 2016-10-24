# Simple REST API with Flask Framework

You can modify this project easily.

Technologies :
    
  - Python 2.7
  - Flask
  - Pewee ORM

Is necessary that you have install MYSQL.
If you want change the db engie you needs to modify the models.py file.
  
### Run local

Install Libraries

```Python
pip install Flask
```

Install Pewee

```Python
pip install peewee
```

Execute Server

```Python
Python manage.py
```

This line execute the Flask sever, by defult this server run in the por 8000.
If you need change the port you needs to modify the config file.

### Methods

-	GET
```Python
curl -i http://localhost:8000/codigo/api/v1.0/courses/1
```

-	POST
```Python
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"New Course", "slug": "new_course", "description": "This is a simple request with POST method"}' http://localhost:8000/codigo/api/v1.0/courses/
```

-	PUT
```Python
curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"new title", "slug": "new_title", "description": "change the description"}' http://localhost:8000/codigo/api/v1.0/courses/1
```

-	DElETE
```Python
curl -X DELETE http://localhost:8000/codigo/api/v1.0/courses/1
```

