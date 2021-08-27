# Library


Features:
- Creating books with multiple authors
- Editing books
- Filtering books
- Saving books from Google Books API
- REST API with filters


# How to use
- Download the repository.

- Create .env file in Library/libraryproject/libraryproject/ it should contain:
```
SECRET_KEY=you_SECRET_KEY
DEBUG=on
GOOGLE_API_KEY=your_API_KEY
```
GOOGLE_API_KEY is needed to be able to save books from Google Books API. 

Google provides instruction how to register an API Key here: [Get an API Key](https://developers.google.com/maps/documentation/maps-static/get-api-key) 


- Start with docker:

cd to /Library and use docker-compose by typing in console
```
docker-compose up
```
- Start with Python:

Preferably create a virtual environment.

cd to /Library/libraryproject
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.
```
pip install -r requirements.txt
```
With requirements installed you can run the app:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Tests
- With docker-compose:
Go into docker-compose.yml file, edit:
```
"python manage.py makemigrations &&
 python manage.py migrate &&
 python manage.py runserver 0:8000"
 ```
and put in pytest command:
 ```
 command: |
      sh -c "pytest"
 ```
next just cd to /Library and use docker-compose by typing in console
 ```
 docker-compose up
 ```
- With python:
After installing app and requirements.txt simply go into /Library/libraryproject and type into console:
  ```
pytest
  ```
