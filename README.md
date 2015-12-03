# SQLAlchemyDatabase

## Introduction

SQLAlchemyDatabase abstracts and simplifies the parts of SQLAlchemy that are
required for every database connection (binding the engine, creating a Session
object, etc.). It also abstracts connections to different database types
(currently SQLite and PostgreSQL) to simplify the startup process.

## Sample Usage

	from sqlalchemy import Column, Integer, String
	from sqlalchemydatabase import SQLiteDatabase

	class User(SQLiteDatabase.Base):
		__tablename__ == 'users'

		id = Column(Integer, primary_key=True)
		name = Column(String, unique=True)
		password = Column(String)

		def __init__(self, id, name, password):
			self.id = id
			self.name = name
			self.password = password

		def __repr__(self):
			return '{}:{}:{}'.format(self.id, self.name, self.password)


	database = SQLiteDatabase(uri='sqlite:///database.sqlite')
	session = database.Session()

	session.add(User(0, 'root', 'passw0rd'))
	session.add(User(1, 'me', 'badpassword'))
	session.commit()
	users = session.query(User).all()
	for user in users:
		print user

