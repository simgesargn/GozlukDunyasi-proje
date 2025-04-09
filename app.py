from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/admin')
def admin():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('admin.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        conn = get_db_connection()
        conn.execute('INSERT INTO products (name, price, image) VALUES (?, ?, ?)', (name, price, image))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))
    return render_template('add_product.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        conn.execute('UPDATE products SET name = ?, price = ?, image = ? WHERE id = ?', (name, price, image, id))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))

    conn.close()
    return render_template('edit_product.html', product=product)

@app.route('/delete/<int:id>')
def delete_product(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)


