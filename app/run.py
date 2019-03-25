from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = "flash message"


@app.route('/')
def Index():
    return redirect(url_for('Login'))


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        db = pymysql.connect("mysql", "dbuser", "prueba.2019", "crud")
        cursor = db.cursor()
        sql = "INSERT INTO students(name, email, phone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, phone))
        db.commit()
        db.close()
        return redirect(url_for('Layout'))


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    db = pymysql.connect("mysql", "dbuser", "prueba.2019", "crud")
    cursor = db.cursor()
    sql = "DELETE FROM students WHERE id=%s"
    cursor.execute(sql, (id_data))
    db.commit()
    db.close()
    return redirect(url_for('Layout'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        db = pymysql.connect("mysql", "dbuser", "prueba.2019", "crud")
        cursor = db.cursor()
        sql = """
               UPDATE students
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
              """
        cursor.execute(sql, (name, email, phone, id_data))
        db.commit()
        db.close()
        flash("Data Updated Successfully")
        return redirect(url_for('Layout'))


@app.route('/login')
def Login():
    return(render_template('login.html'))


@app.route('/layout')
def Layout():
    db = pymysql.connect("mysql", "dbuser", "prueba.2019", "crud")
    cursor = db.cursor()
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return(render_template('template.html',
                           user="jcramirez",
                           students=results))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
