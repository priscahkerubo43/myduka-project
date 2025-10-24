from flask import Flask,render_template
# instance of the Flask class
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def prods():
    return render_template('products.html')

# create routes for sales and stock
@app.route('/sales')
def sale():
    return render_template('sales.html')

@app.route('/stock')
def stk():
    return render_template('stock.html')

app.run()