import psycopg2

# ---- Connect to the Database ---- #
try:
	conn = psycopg2.connect(database='dbmain', user='dbuser', password='dbuser@6814', host='127.0.0.1', port='5432')
except BaseException as err:
	print(f"Could not connect to the database:\n\n{err}")
	input()
	raise
cur = conn.cursor()


# ---- Define User Permission Classes ---- #

class Class1():
	def do_one(self, arg):
		print("This is Class #1")

class Class2():
	def do_two(self, arg):
		print("This is Class #2")

class Class3():
	def do_three(self, arg):
		print("This is Class #3")

class Admin(Class1, Class2, Class3):
	def do_admin(self, arg):
		print("You are an Admin!")

perm_classes = {
	'class1': Class1,
	'class2': Class2,
	'class3': Class3,
	'admin' : Admin,
}

def get_permissions(user):
	cur.execute(f"SELECT perm_class FROM db_users WHERE username='{user}';")
	user_class = cur.fetchone()[0]
	return perm_classes[user_class]

