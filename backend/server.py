import os

from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from queries import resolve_todo, resolve_todos
from mutations import resolve_create_todo, resolve_delete_todo, resolve_mark_done, resolve_update_due_date

query = ObjectType('Query')
query.set_field('todo', resolve_todo)
query.set_field('todos', resolve_todos)

mutation = ObjectType('Mutation')
mutation.set_field('createTodo', resolve_create_todo)
mutation.set_field('deleteTodo', resolve_delete_todo)
mutation.set_field('markDone', resolve_mark_done)
mutation.set_field('updateDueDate', resolve_update_due_date)

type_defs = load_schema_from_path('schema.graphql')
schema = make_executable_schema(
	type_defs, query, mutation, snake_case_fallback_resolvers
)

app = Flask(__name__)
app.debug = True

engine = create_engine(f'sqlite:///{os.getcwd()}/database.db')
session_factory = sessionmaker(bind=engine)
session = flask_scoped_session(session_factory, app)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/graphql', methods=['GET'])
def graphql_playground():
	return PLAYGROUND_HTML, 200

@app.route('/graphql', methods=['POST'])
def graphql_server():
	data = request.get_json()

	success, result = graphql_sync(
		schema,
		data,
		context_value=request,
		debug=app.debug
	)

	status_code = 200 if success else 400
	return jsonify(result), status_code

if __name__ == "__main__":
    app.run()
