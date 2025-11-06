from flask import Flask, render_template, request, redirect, url_for
from database import fetch_data, insert_products, insert_sales, insert_stock, product_profit, product_sale, sale_day, connect, curr, profit_day, conn, insert_users, check_email
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
@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    # checking method whether post or get
    if request.method == 'POST':
        pname = request.form['name']
        bp = request.form['buying_price']
        sp = request.form['selling_price']
        # storing them in one variable
        new_product = (pname, bp, sp)
        # print(new_product)
        # insert to database
        insert_products(new_product)
    return redirect(url_for('prods'))


# create routes for sales and stock


@app.route('/sales')
def sale():
    sales = fetch_data('sales')
    # fetch products
    products = fetch_data('products')
    # print(sales)
    return render_template('sales.html', mysales=sales, products=products)

# creating a python function that receives sales from the ui to the severe side then to the database


@app.route('/add_sale', methods=['GET', 'POST'])
def add_sale():
    # checking method whether post or get
    if request.method == 'POST':
        pid = request.form['product_id']
        sq = request.form['quantity']
        # storing them in one variable
        new_sales = (pid, sq)
        # print(new_sales)
        # insert to database
        insert_sales(new_sales)
    return redirect(url_for('sale'))


@app.route('/stock')
def stk():
    stock = fetch_data('stock')
    # fetching the products
    products = fetch_data('products')
    # print(stock)
    return render_template('stock.html', mystock=stock, products=products)

# create a python function that receives stock from the ui to the server then to the database


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    # checking method whether post or get
    if request.method == 'POST':
        pid = request.form['product_id']
        sq = request.form['squantity']
        # storing them in one variable
        new_stock = (pid, sq)
        # print(new_stock)
        # insert to database
        insert_stock(new_stock)
    return redirect(url_for('stk'))

# dashboard route


@app.route('/dashboard')
def dashboard():
    profit = product_profit()
    # print(profit)
    product_names = []
    product_profits = []
    for i in profit:
        product_names.append(i[0])
        product_profits.append(float(i[2]))

    sales = product_sale()
    # print(sales)
    pnames = []
    psale = []
    for i in sales:
        pnames.append(i[0])
        psale.append(float(i[2]))

    # sales day
    sday = sale_day()
    # print(sday)
    date = []
    sl = []
    for i in sday:
        date.append(str(i[0]))
        sl.append(float(i[1]))

    # profit day
    pday = profit_day()
    # print(profit_day)
    d = []
    p = []
    for i in pday:
        d.append(str(i[0]))
        p.append(float(i[1]))
    print(p)
    print(d)

    return render_template('dashboard.html', product_profits=product_profits, product_names=product_names, psale=psale, pnames=pnames, sl=sl, date=date, p=p, d=d,)


# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        new_user = (username, email, password)
        # confirm email
        check = check_email(email)
        if check == None:
            # check user
            insert_users(new_user)
            print('registeration successful')
            return redirect(url_for('login'))
        else:
            print('user exists,use a different email or login')
            return render_template('register.html')

    return render_template('register.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # check email
        check = check_email(email)
        if check == None:
            print('user does not exist register')
            return redirect(url_for('register'))
        else:
            # check if password matches users data
            if password == check[3]:
                print('login successfully')
                return redirect(url_for('dashboard'))
            else:
                print('Wrong password or email')
                return redirect(url_for('login.html'))
    return render_template('login.html')


app.run(debug=True)
