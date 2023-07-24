from flask import Flask,render_template,request,url_for, redirect
from database import get_database,connect_to_database
import sqlite3
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    # sql = connect_to_database()
    sql = sqlite3.connect('C:/Users/Lenovo/Desktop/todoapp/todoapp.db')
    cursor = sql.cursor()
    task = cursor.execute("select * from todolist")
    alltasks = task.fetchall()
    return render_template("index.html",alltasks=alltasks)

@app.route('/inserttask',methods=["POST","GET"])
def inserttask():
    if request.method == "POST":
        #get the task enter my user from the form
        enteredtask =request.form["todaystask"]
        # sql = connect_to_database()
        sql = sqlite3.connect('C:/Users/Lenovo/Desktop/todoapp/todoapp.db')
        cursor = sql.cursor()
        cursor.execute("insert into todolist(task) values(?)",[enteredtask])
        sql.commit()
        return redirect(url_for("index"))
    return render_template("index.html")
@app.route('/deletetask/<int:id>',methods=["POST","GET"])
def deletetask(id):
    if request.method == "GET":
        sql = sqlite3.connect('C:/Users/Lenovo/Desktop/todoapp/todoapp.db')
        cursor = sql.cursor()
        cursor.execute("delete from todolist where id = ?",[id])
        
        sql.commit()
        return redirect(url_for("index"))

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)