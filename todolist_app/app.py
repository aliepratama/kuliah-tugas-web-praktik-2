from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todolist'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list/')
def list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM todo")
    data = cur.fetchall()
    print('DATA>>>>>>>>>>>>>', data)
    cur.close()
    return render_template('list.html', users=data)


@app.route('/form/')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
    