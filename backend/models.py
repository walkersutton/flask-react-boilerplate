from sqlalchemy import Boolean, Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
	__tablename__ = 'Todo'
	id = Column(Integer, primary_key=True)
	description = Column(String)
	completed = Column(Boolean, default=False)
	due_date = Column(Date)

	def to_dict(self):
		return {
			'id': self.id,
			'description': self.description,
			'completed': self.completed,
			'due_date': self.due_date
		}
