# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
# from datetime import datetime

# app = Flask(__name__)

# # ---------- Initialize Database on Startup ----------
# def init_db():
#     conn = sqlite3.connect('database.db')
#     cur = conn.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS bills (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             customer TEXT,
#             product TEXT,
#             quantity INTEGER,
#             price REAL,
#             gst REAL,
#             total REAL,
#             payment TEXT,
#             date TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# init_db()

# # ---------- Home Route ----------
# @app.route('/')
# def home():
#     return render_template('home.html')

# # ---------- Billing Form ----------
# @app.route('/billing')
# def billing():
#     return render_template('index.html')

# # ---------- Generate Invoice ----------
# @app.route('/generate', methods=['POST'])
# def generate():
#     data = request.form
#     customer = data['customer']
#     product = data['product']
#     quantity = int(data['quantity'])
#     price = float(data['price'])
#     gst_rate = float(data['gst'])
#     payment = data['payment']
#     date = data['date'] or datetime.now().strftime('%Y-%m-%d')

#     # Calculate GST and Total
#     gst = quantity * price * gst_rate / 100
#     total = quantity * price + gst

#     # Store in database
#     conn = sqlite3.connect('database.db')
#     conn.execute('''
#         INSERT INTO bills (customer, product, quantity, price, gst, total, payment, date)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#     ''', (customer, product, quantity, price, gst, total, payment, date))
#     conn.commit()
#     conn.close()

#     # Render invoice page
#     return render_template('invoice.html',
#                            customer=customer,
#                            product=product,
#                            quantity=quantity,
#                            price=price,
#                            gst=gst,
#                            total=total,
#                            payment=payment,
#                            date=date)

# # ---------- View All Invoices ----------
# @app.route('/all-bills')
# def all_bills():
#     conn = sqlite3.connect('database.db')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM bills ORDER BY date DESC")
#     bills = cur.fetchall()
#     conn.close()
#     return render_template('all_bills.html', bills=bills)

# # ---------- Search Invoices ----------
# @app.route('/search')
# def search():
#     query = request.args.get('query')
#     results = []
#     if query:
#         conn = sqlite3.connect('database.db')
#         cur = conn.cursor()
#         cur.execute('''
#             SELECT * FROM bills 
#             WHERE customer LIKE ? OR product LIKE ?
#         ''', (f'%{query}%', f'%{query}%'))
#         results = cur.fetchall()
#         conn.close()
#     return render_template('search.html', results=results)

# # ---------- Error Handling ----------
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# # ---------- Run the App ----------
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# ---------- Initialize Database on Startup ----------
def init_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            product TEXT,
            quantity INTEGER,
            price REAL,
            gst REAL,
            total REAL,
            payment TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---------- Home Route ----------
@app.route('/')
def home():
    return render_template('home.html')

# ---------- Billing Form ----------
@app.route('/billing')
def billing():
    return render_template('index.html')

# ---------- Generate Invoice ----------
@app.route('/generate', methods=['POST'])
def generate():
    data = request.form
    customer = data['customer']
    product = data['product']
    quantity = int(data['quantity'])
    price = float(data['price'])
    gst_rate = float(data['gst'])
    payment = data['payment']
    date = data['date'] or datetime.now().strftime('%Y-%m-%d')

    # Calculate GST and Total
    gst = quantity * price * gst_rate / 100
    total = quantity * price + gst

    # Store in database
    conn = sqlite3.connect('database.db')
    conn.execute('''
        INSERT INTO bills (customer, product, quantity, price, gst, total, payment, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (customer, product, quantity, price, gst, total, payment, date))
    conn.commit()
    conn.close()

    # Render invoice page
    return render_template('invoice.html',
                           customer=customer,
                           product=product,
                           quantity=quantity,
                           price=price,
                           gst=gst,
                           total=total,
                           payment=payment,
                           date=date)

# ---------- View All Invoices ----------
@app.route('/all-bills')
def all_bills():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bills ORDER BY date DESC")
    bills = cur.fetchall()
    conn.close()
    return render_template('all_bills.html', bills=bills)

# ---------- Search Invoices ----------
@app.route('/search')
def search():
    query = request.args.get('query')
    results = []
    if query:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM bills 
            WHERE customer LIKE ? OR product LIKE ?
        ''', (f'%{query}%', f'%{query}%'))
        results = cur.fetchall()
        conn.close()
    return render_template('search.html', results=results)

# ---------- Error Handling ----------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# ---------- Run the App ----------
if __name__ == '__main__':
    port=int(os.environ.get('PORT',10000))
    app.run(host='0.0.0.0',port=port)