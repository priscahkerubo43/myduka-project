# import psycopg2
import psycopg2

# connect to postgress database
connect = psycopg2.connect(
    host='localhost',
    user='postgres',
    dbname='myduka_db',
    port=5432,
    password='prisca1416'
)
# declare cursor
curr = connect.cursor()
# Commit
conn = connect.commit

# # database operations
# curr.execute('select * from products;')
# data=curr.fetchall()
# print(data)

# # display sales on terminal
# curr.execute('select * from sales;')
# data=curr.fetchall()
# print(data)

# # display stock on terminal
# curr.execute('select * from stock;')
# data=curr.fetchall()
# print(data)

# function to insert product


def fetch_data(table_name):
    curr.execute(f'select * from {table_name}')
    data = curr.fetchall()
    return data


products = fetch_data('products')
# print(products)
stock = fetch_data('stock')
# print(stock)
sales = fetch_data('sales')
# print(sales)

# function to insert products


def insert_products(values):
    query = 'insert into products(name,buying_price,selling_price)values(%s,%s,%s);'
    curr.execute(query, values)
    connect.commit()


new_product = ('mango', 60, 100)
insert_products(new_product)
products = fetch_data('products')
# print(products)


def insert_sales(values):
    query = 'insert into sales(pid,quantity,created_at)values(%s,%s,now());'
    curr.execute(query, values)
    connect.commit()


new_sale = [6, 10]
sales = fetch_data('sales')
# print(sales)


def insert_stock(values):
    query = 'insert into stock(pid,stock_quantity)values(%s,%s);'
    curr.execute(query, values)
    connect.commit()


new_stock = [2, 20]
stock = fetch_data('stock')
# print(stock)


def product_profit():
    query = 'select p.name,p.id,sum((p.selling_price-p.buying_price)*s.quantity) as total_profit from sales s inner join products p on s.pid=p.id group by p.name,p.id;'
    curr.execute(query)
    profit = curr.fetchall()
    return profit


def product_sale():
    query = 'select p.name,p.id,sum(p.selling_price*s.quantity)as profit from sales as s inner join products as p on s.pid=p.id group by p.name,p.id;'
    curr.execute(query)
    sales = curr.fetchall()
    return sales


def profit_day():
    query = 'select date(sales.created_at) as sale_date,sum((products.selling_price-products.buying_price)*sales.quantity) as total_profit from sales  inner join products  on sales.pid=products.id group by date(sales.created_at) order by date(sales.created_at);'
    curr.execute(query)
    dayprofit = curr.fetchall()
    return dayprofit


def sale_day():
    query = 'select date(s.created_at) AS sale_date, sum(p.selling_price*s.quantity)as profit from sales as s inner join products as p on s.pid=p.id group by date(s.created_at);'
    curr.execute(query)
    saleprofit = curr.fetchall()
    return saleprofit


def insert_users(user_values):
    query = 'insert into users(full_name,email,password)values(%s,%s,%s);'
    curr.execute(query, user_values)
    connect.commit

# check if user exsists


def check_email(email):
    query = 'select * from users where email=%s'
    curr.execute(query, (email,))
    data = curr.fetchone()
    return data
