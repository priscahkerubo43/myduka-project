from flask import Flask, render_template,request,redirect,url_for
from database import fetch_data,insert_products,insert_sales,insert_stock
# instance of the Flask class
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def prods():
    prods = fetch_data('products')
    # print(prods)
    return render_template('products.html', myproducts=prods)


# create a python function that receives data from ui to the severside
@app.route('/add_products', methods=['GET','POST'])
def add_products():
    # checking method whether post or get
    if request.method=='POST':
        pname=request.form['name']
        bp=request.form['buying_price']
        sp=request.form['selling_price']
        # storing them in one variable
        new_product=(pname,bp,sp)
        # print(new_product)
        # insert to database
        insert_products(new_product)
    return redirect (url_for('prods'))


   

# create routes for sales and stock


@app.route('/sales')
def sale():
    sales = fetch_data('sales')
    # print(sales)
    return render_template('sales.html', mysales=sales)

# creating a python function that receives sales from the ui to the severe side then to the database
@app.route('/add_sale', methods=['GET','POST'])
def add_sale():
    # checking method whether post or get
    if request.method=='POST':
        pid=request.form['product_id']
        sq=request.form['quantity']
        # storing them in one variable
        new_sales=(pid,sq)
        # print(new_sales)
        # insert to database
        insert_sales(new_sales)
    return redirect (url_for('sale'))


@app.route('/stock')
def stk():
    stock = fetch_data('stock')
    # print(stock)
    return render_template('stock.html', mystock=stock)

# create a python function that receives stock from the ui to the server then to the database

@app.route('/add_stock', methods=['GET','POST'])
def add_stock():
    # checking method whether post or get
    if request.method=='POST':
        pid=request.form['product_id']
        sq=request.form['squantity']
        # storing them in one variable
        new_stock=(pid,sq)
        # print(new_stock)
        # insert to database
        insert_stock(new_stock)
    return redirect (url_for('stk'))


app.run(debug=True)
