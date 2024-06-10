from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/home')
def home():
    return  render_template_string("""
    <html>
    <head>
        <title>Home</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #333;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin: 10px 0;
            }
            a {
                text-decoration: none;
                color: #0066cc;
                font-size: 18px;
            }
            a:hover {
                text-decoration: underline;
            }
            .container {
                width: 50%;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                margin-top: 50px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the Home Page</h1>
            <ul>
                <h3><li><a href="/addproduct">Add Product</a></li></h3>
                <h3><li><a href="/removeproduct">Remove Product</a></li></h3>
                <h3><li><a href="/updateproduct">Update Product</a></li></h3>
            </ul>
        </div>
    </body>
    </html>
    """)

@app.route('/addproduct', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        product_name = request.form['productname']
        product_price = request.form['price']
        conn = get_db_connection()
        conn.execute('INSERT INTO products (name, price) VALUES (?, ?)', (product_name, product_price))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template_string("""
    <html>
    <head>
        <title>Add Product</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #333;
            }
            .container {
                width: 50%;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                margin-top: 50px;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label, input {
                margin-bottom: 10px;
                font-size: 16px;
            }
            input[type="text"] {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            input[type="submit"] {
                background-color: #0066cc;
                color: #fff;
                padding: 10px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #004080;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Add Product Page</h1>
            <form action="/addproduct" method="post">
                <label for="productname">Product Name:</label><br>
                <input type="text" id="productname" name="productname"><br>
                <label for="price">Price:</label><br>
                <input type="text" id="price" name="price"><br><br>
                <input type="submit" value="Add Product">
            </form>
        </div>
    </body>
    </html>
    """)

@app.route('/removeproduct', methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        product_id = request.form['productid']
        conn = get_db_connection()
        conn.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template_string("""
    <html>
    <head>
        <title>Remove Product</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #333;
            }
            .container {
                width: 50%;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                margin-top: 50px;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label, input {
                margin-bottom: 10px;
                font-size: 16px;
            }
            input[type="text"] {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            input[type="submit"] {
                background-color: #0066cc;
                color: #fff;
                padding: 10px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #004080;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Remove Product Page</h1>
            <form action="/removeproduct" method="post">
                <label for="productid">Product ID:</label><br>
                <input type="text" id="productid" name="productid"><br><br>
                <input type="submit" value="Remove Product">
            </form>
        </div>
    </body>
    </html>
    """)

@app.route('/updateproduct', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        product_id = request.form['productid']
        new_name = request.form['productname']
        new_price = request.form['price']
        conn = get_db_connection()
        conn.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (new_name, new_price, product_id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template_string("""
    <html>
    <head>
        <title>Update Product</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #333;
            }
            .container {
                width: 50%;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                margin-top: 50px;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label, input {
                margin-bottom: 10px;
                font-size: 16px;
            }
            input[type="text"] {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            input[type="submit"] {
                background-color: #0066cc;
                color: #fff;
                padding: 10px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #004080;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Update Product Page</h1>
            <form action="/updateproduct" method="post">
                <label for="productid">Product ID:</label><br>
                <input type="text" id="productid" name="productid"><br>
                <label for="productname">New Product Name:</label><br>
                <input type="text" id="productname" name="productname"><br>
                <label for="price">New Price:</label><br>
                <input type="text" id="price" name="price"><br><br>
                <input type="submit" value="Update Product">
            </form>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
