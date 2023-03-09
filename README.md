# Introduction

A simple rest api for an elearning platform

### Main features

* Create courses

* Create Modules for courses

* Create lessons for a specific module

* Create contents for the module

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/danielerat/solvit_elearning.git
    $ cd solvit_elearning
    
# Install the project and you named it...

To install this project follow the following steps:

### Install dependencies and the env

To install the dependencies and setup your virtual environment use

    $ pipenv install 
    
Make Your migrations

    $ python manage.py makemigrations
    
    $ python manage.py migrate
      
### running your server
You can now run the development server:

    $ python manage.py runserver