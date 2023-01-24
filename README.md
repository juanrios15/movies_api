# Movies API
## Installation
Start a virtual environment and execute the following commands:

- pip install -r requirements.txt
- python manage.py migrate
- python manage.py loaddata data
- python manage.py test apps/
- python manage.py runserver

## Usage
### Register using the following endpoint:  
(**POST**) http://localhost:8000/users/users/  
Body must include email and password, example:
```
{
    "email": "carlos@burgos.com"  
    "password": "12345678910aB@"
}
```
### Login to obtain an access token
(**POST**) http://localhost:8000/users/login/  
Body must include email and password as before

*Now you can access the API including Authorization header with your token with 'Token' as prefix.* 
Example: **Authorization: Token 024a1be3f6738543d6b1e25b64c76c091c9ec11f**

### Create a movie
(**POST**) http://localhost:8000/movies/movies/  
Body Example:
```
{ 
    "name": "Taxi Driver", 
    "summary": "Movie about a taxi driver", 
    "release_date": "1968-01-01", 
    "directed_by": "Martin Scorcese", 
    "running_time": 157, 
    "language": "English", 
    "is_private": "false" 
}
```
### List movies (you can only access to public or your own movies)
(**GET**) http://localhost:8000/movies/movies/
### Get one movie
(**GET**) http://localhost:8000/movies/movies/{id}/
### Modify one movie
(**UPDATE/PATCH**) http://localhost:8000/movies/movies/{id}/
