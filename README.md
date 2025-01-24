# Flask Blog

A plug&play demo web app demonstrating 
- user registration 
- ORM techniques 
- content CRUD operations 
- Jinja templating


## Installation

Make sure you have Python 3.11 installed, as well as the Python library [pipenv](https://pypi.org/project/pipenv/).

Clone or download this project to your machine. Take a look at the [.env.example](.env.example) file. You will need to replace the placeholder variables with your personal data. Then save and rename the file to `.env`.

Open a terminal within the project directory and execute the following command:

```
pipenv install
```
This will create a virtual environment with the necessary dependencies.

## Run

Within your terminal execute the following commands:

```
pipenv shell
```
```
flask --app app run
```

You can access the app using your favorite browser on `http://localhost:5000`.