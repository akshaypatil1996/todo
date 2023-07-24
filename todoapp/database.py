import sqlite3
from flask import g
def connect_to_database():
    sql = sqlite3.connect('C:/Users/Lenovo/Desktop/todoapp/todoapp.db')
    cursor = sql.cursor()
    cursor.row_factory = sqlite3.Row
    return cursor
def get_database():
    if not hasattr(g,"todo_db"):
        g.todo_app = connect_to_database
    return g.todo_app