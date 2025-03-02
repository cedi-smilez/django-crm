import mysql.connector

data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql@123.'
)

# preparing a cursor object
cursor_object = data_base.cursor()

# create a database
cursor_object.execute('CREATE DATABASE smilezdb')
print('ALL DONE!')
