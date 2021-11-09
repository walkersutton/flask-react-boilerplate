from datetime import datetime
from ariadne import convert_kwargs_to_snake_case
from flask_sqlalchemy_session import current_session

from models import Todo

@convert_kwargs_to_snake_case
def resolve_create_todo(obj, info, description, due_date):
	try :
		due_date = datetime.strptime(due_date, '%d-%m-%Y').date()
		todo = Todo(description=description, due_date=due_date)
		current_session.add(todo)
		current_session.commit()	
		payload = {
			'success': True,
			'todo': todo.to_dict()
		}
	except ValueError:
		payload = {
			'success': False,
			'errors': [f'Incorrect date format provided. Date should be in the format of dd-mm-yyyy']
		}
	return payload

@convert_kwargs_to_snake_case
def resolve_delete_todo(obj, info, todo_id):
	try:
		todo = current_session.query(Todo).get(todo_id)
		current_session.delete(todo)
		current_session.commit()
		payload = {'success': True}
	except AttributeError:
		payload = {
			'success': False,
			'errors': [f'Todo matching id {todo_id} was not found']
		}
	return payload

@convert_kwargs_to_snake_case
def resolve_mark_done(obj, info, todo_id):
	try:
		todo = current_session.query(Todo).get(todo_id)
		todo.completed = True
		current_session.add(todo)
		current_session.commit()
		payload = {
			'success': True,
			'todo': todo.to_dict()
		}
	except AttributeError:
		payload = {
			'success': False,
			'errors': [f'Todo matching id {todo_id} was not found']
		}
	return payload

@convert_kwargs_to_snake_case
def resolve_update_due_date(obj, info, todo_id, new_date):
	try:
		todo = current_session.query(Todo).get(todo_id)
		if todo:
			todo.due_date = datetime.strptime(new_date, '%d-%m-%Y').date()
		current_session.add(todo)
		current_session.commit()
		payload = {
			'success': True,
			'todo': todo.to_dict()
		}
	except ValueError:
		payload = {
			'success': False,
			'errors': [f'Incorrect date format provided. Date should be in the format of dd-mm-yyyy']
		}
	except AttributeError:
		payload = {
			'success': False,
			'errors': [f'Todo matching id {todo_id} was not found']
		}
	return payload
