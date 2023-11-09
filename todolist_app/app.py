from flask import Flask, render_template, request, redirect
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


@app.route('/list/', methods=['GET'])
def list():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM todo ORDER BY kategori")
        data = cur.fetchall()
        print('DATA>>>>>>>>>>>>>', data)
        cur.close()
        return render_template('list.html', lists=data, count=len(data))


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        kategori_list = ('Penting', 'Sedang', 'Biasa')
        nama_kegiatan = request.form['nama_kegiatan']
        kategori = request.form['kategori']
        print(nama_kegiatan, kategori)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO todo (nama_kegiatan, kategori) VALUES (%s, %s)', (nama_kegiatan, kategori_list.index(kategori)))
        mysql.connection.commit()
        cur.close()
        return redirect('/list/')
    return render_template('form.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM todo WHERE id=%s", (id, ))
        data = cur.fetchall()
        print('DATA>>>>>>>>>>>>>', data)
        cur.close()
        return render_template('form_edit.html', todo=data, id=id)
    elif request.method == 'POST':
        kategori_list = ('Penting', 'Sedang', 'Biasa')
        nama_kegiatan = request.form['nama_kegiatan']
        kategori = request.form['kategori']
        print(nama_kegiatan, kategori)
        cur = mysql.connection.cursor()
        cur.execute('UPDATE todo SET nama_kegiatan=%s, kategori=%s WHERE id=%s', (nama_kegiatan, kategori_list.index(kategori), id))
        mysql.connection.commit()
        cur.close()
        return redirect('/list/')

@app.route('/delete/<id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM todo WHERE id=%s', (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/list/')

if __name__ == '__main__':
    app.run(debug=True)
    