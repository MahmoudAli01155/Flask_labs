# RUN THIS FILE WITH python test.py read_users
from myPackage import db,app
import sys
from myPackage.models import Student, Supject

# create database
def create_db():
	with app.app_context():
		# you will have instance folder with site.db inside
		db.create_all()

# -------------------------- CRUD OPERATIONS --------------------------
# Create operation
def create_student():
	with app.app_context():
		student = Student(username='mahmoud2', email='mahmoud2@gmail.com', password='123')
		db.session.add(student)
		db.session.commit()

# Create operation
def create_supjects():
	with app.app_context():
		# student = Student.query.first()
		supject1 = Supject(title='testtitle', content='testcontent', student_id=4)
		supject2 = Supject(title='testtitle2', content='testcontent2', student_id=5)
		db.session.add(supject1)
		db.session.add(supject2)
		db.session.commit()

# Read operation
def read_student():
	with app.app_context():
		student = Student.query.first()
		print(student.posts[0].content)

# Read supjects
def read_supjects():
	with app.app_context():
		supjects = Supject.query.first()
		print(supjects.title[0].content)
		print(supjects.student_id[0].content)

# Update operation
def update_student():
	with app.app_context():
		print("Get Specific student")
		student = Student.query.filter_by(username="mahmoud2").first()
		print(student)
		student.email = 'asd@gmail.com'
		db.session.commit()
		student = Student.query.filter_by(username="mahmoud2").first()
		print("\nAfter Change")
		print(student)

# Delete operation
def delete_student():
	with app.app_context():
		student = Student.query.all()
		print(student)

		student = Student.query.filter_by(username="mahmoud2").first()
		db.session.delete(student)
		db.session.commit()

		student = Student.query.all()
		print(student)

# snippet to allow us to run funcs from terminal with "python test.py print_func"
if __name__ == '__main__':
	globals()[sys.argv[1]]()