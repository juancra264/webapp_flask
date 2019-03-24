from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)


@app.route('/')
def Index():
    db = pymysql.connect("mysql", "dbuser", "prueba.2019", "crud")
    cursor = db.cursor()
    sql = "SELECT * FROM students WHERE id = 14"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    #return render_template('index.html')
    return render_template('index3.html', results=results)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students(name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
