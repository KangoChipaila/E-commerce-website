from flask import Flask, render_template, flash, redirect, request, url_for

app = Flask(__name__)
app.secret_key = 'Navennaguduri'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('product page.html')

@app.route('/men')
def men_clothing():
    return render_template('men.html')

@app.route('/women')
def women_clothing():
    return render_template('women.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/my-account')
def my_account():
    return render_template('account.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/place_order', methods=['POST'])
def place_order():

    shipping_info = {
        'name': request.form.get('name'),
        'address': request.form.get('address'),
        'city': request.form.get('city'),
        'state': request.form.get('state'),
        'zip': request.form.get('zip'),
        'country': request.form.get('country'),
        'email': request.form.get('email')
    }
    payment_info = {
        'card_number': request.form.get('card_number'),
        'expiry': request.form.get('expiry'),
        'cvv': request.form.get('cvv')
    }

    flash('Order placed successfully!', 'success')
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)