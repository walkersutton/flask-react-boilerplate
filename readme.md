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
npx TODO
```

## Libraries

### Backend

* [Flask](https://flask.palletsprojects.com/) - a micro web framework written in Python
* [GraphQL](https://graphql.org/) - a query language for APIs and a runtime for fulfilling those queries with your existing data
	* [ariadne](https://ariadnegraphql.org/) - a Python library for implementing GraphQL servers
* [SQLite](https://www.sqlite.org/index.html) - a small, fast, self-contained, high-reliability, full-featured, SQL database engine
	* [SQLAlchemy](https://www.sqlalchemy.org/) - a Python SQL toolkit
		* [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - an extension for Flask that adds support for SQLAlchemy
		* [Alembic](https://alembic.sqlalchemy.org/en/latest/) - a lightweight database migration tool for SQLAlchemy
			* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest) - an extension that handles database migrations using Alembic

### Frontend
* [React](https://reactjs.org/) - a JavaScript library for building user interfaces
	* [Create React App](https://github.com/facebook/create-react-app) - a tool for starting new single-page React applications

## Resources

### Backend
* [Flask GraphQL Example](https://github.com/andreisoriga/flask-graphql-example) by [@andreisoriga](https://github.com/andreisoriga)
* [Build a GraphQL API with Python, Flask and Ariadne](https://www.twilio.com/blog/graphql-api-python-flask-ariadne) by [@mistr_qra](https://twitter.com/mistr_qra)
	* [GitHub Repo](https://github.com/mrkiura/todo-api-graphql)
* [Flask Project Structure](https://codersdiaries.com/blog/flask-project-structure)
* [Flask Migrate Example 1](https://github.com/CristianoYL/flask-migrate-example) by [@CristianoYL](https://github.com/CristianoYL)
* [Flask Migrate Example 2](https://github.com/RobertBoes/flask-migrate-example) by [@Robert_Boes](https://twitter.com/robert_boes)

### Frontend
* [React + Flask + GraphQL](https://blog.sethcorker.com/how-to-create-a-react-flask-graphql-project/) by [@Darth_Knoppix](https://twitter.com/darth_knoppix)
	* [GitHub Repo](https://github.com/Darth-Knoppix/flask-graphql-react)
