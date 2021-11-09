from flask_sqlalchemy_session import current_session
from ariadne import convert_kwargs_to_snake_case

from models import Todo

@convert_kwargs_to_snake_case
def resolve_todo(obj, info, todo_id):
	try:
		todo = current_session.query(todo).get(todo_id)
		payload = {
			'success': True,
			'todo': todo.to_dict()
		}
	except AttributeError:
		payload = {
			'success': False,
			'errors': [f'Todo item matching id {todo_id} not found']
		}
	return payload

def resolve_todos(obj, info):
	try:
		todos = [todo.to_dict() for todo in current_session.query(Todo).all()]
		payload = {
			'success': True,
			'todos': todos
		}
	except Exception as e:
		payload = {
			'success': False,
			'errors': [str(e)]
		}
	return payload
