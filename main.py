from flask import Flask, render_template
from database import fetch_data
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

# create routes for sales and stock


@app.route('/sales')
def sale():
    sales = fetch_data('sales')
    # print(sales)
    return render_template('sales.html', mysales=sales)


@app.route('/stock')
def stk():
    stock = fetch_data('stock')
    # print(stock)
    return render_template('stock.html', mystock=stock)


app.run()
