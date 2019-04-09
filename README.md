# inn-invictus

### Badges
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9bda5b60dd824e34b4a308defb65af71)](https://www.codacy.com/app/3Nakajugo/inn-invictus?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mwinel/inn-invictus&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/sanya-kenneth/inn-invictus/badge.svg?branch=develop)](https://coveralls.io/github/sanya-kenneth/inn-invictus?branch=develop)
=======
## Introduction

INN is a media app that enables Independent Journalists share their news stories with the rest of the world .

# Features!

  - user should be able to create account.[signup](http://127.0.0.1:8000/api/v1/auth/signup/)
  - user should be able to login
  - user(journalist) should be able to create a story.
  - user(journalist) should be able to delete a story.
  - user(journalist) should be able to update a story.
  - user(journalist) should be able to create a story.
  - moderator should be able to comment on story.
  - admin should be able to approve story.

### Technologies
- [Python 3.6](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.
- [Git](https://git-scm.com/) - Git is a distributed version-control system for tracking changes in source code during software development.
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) - A tool to create isolated Python environments.
- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [Postgresql](https://www.postgresql.org/) - PostgreSQL, often simply Postgres, is an open source object-relational database management system

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Ensure you have the following softwares to run this application.

### Installation

1. Clone this repository by running
```sh 
$ git clone https://github.com/mwinel/inn-invictus.git
```
2. Navigate into the project folder
```sh
$ cd inn-invictus
```
3. Create  Virtual Environment by running
```sh
$ virtualenv name-of-virtualenv
```
4. Activate the virtual environment
```sh 
$ source venv/bin/activate
```
5. Install required depenencies by running
```sh 
$ pip install -r requirements.txt
```
6. make migrations
 ```sh 
 $ python manage.py migrate
 ```
7. Launch / Run the development server.
```sh
$ python manage.py runserver
```

### Running the tests
```sh
$ python manage.py test -v 
```
1. To get the test coverage run.
```sh
$ coverage run manage.py test -v 2
```
2. To get the test report run.
```sh
coverage html
```

authors
---
> [Edna Nakajugo](https://github.com/3Nakajugo) || 
> [Nelson Mwirumubi](https://github.com/mwinel) || 
> [Jean Mark Kaboha](https://github.com/KabohaJeanMark) || 
> [Joel Patrick Mugaya](https://github.com/PatrickMugayaJoel) || 
> [James Francis Kisuule](https://github.com/engjames)

# Acknowledgements
> [Nelson Mwirumubi](https://github.com/mwinel)


  



