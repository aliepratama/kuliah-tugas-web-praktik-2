from flask import Flask, render_template, request
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


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nama_kegiatan = request.form['nama_kegiatan']
        kategori = request.form['kategori']
        print(nama_kegiatan, kategori)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO todo (nama_kegiatan, kategori) VALUES (%s, %s)', (nama_kegiatan, kategori))
        mysql.connection.commit()
        cur.close()
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
    