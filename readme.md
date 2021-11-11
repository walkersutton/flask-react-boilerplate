# Flask React Todo App

## Quick Start

### Clone Repo

```sh
git clone https://github.com/walkersutton/flask-react-todo-app.git
cd flask-react-todo-app
```

### Flask Backend Set Up

```sh
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db init
flask db migrate -m 'Initial migration.'
flask db upgrade
```

### Run Flask Backend
```sh
source venv/bin/activate
export FLASK_APP=app.py
flask run
```

### Run React Frontend
**In a new shell**, let's set up React.

```sh
cd frontend
npx 
```

## TODO
* lint
* will probably want to add some sort of migration script, but not now

## Resources

#### React Resources
* [https://blog.sethcorker.com/how-to-create-a-react-flask-graphql-project/]
* [https://github.com/Darth-Knoppix/flask-graphql-react/blob/master/client/src/App.js]

#### Ariadne, GraphQL, and Flask Resources
* [https://github.com/andreisoriga/flask-graphql-example/blob/master/models]
* [https://www.twilio.com/blog/graphql-api-python-flask-ariadne.py]
* [https://github.com/mrkiura/todo-api-graphql/blob/master/api/mutations.py]
* [https://codersdiaries.com/blog/flask-project-structure]
* [https://github.com/CristianoYL/flask-migrate-example]
* [https://github.com/RobertBoes/flask-migrate-example]
