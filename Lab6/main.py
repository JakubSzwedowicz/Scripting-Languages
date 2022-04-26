from flask import Flask, request, render_template
from datetime import datetime


app = Flask(__name__)


class Currency:
    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag


    def __repr__(self):
        return '<Currency {}>.format(self.code)'


class CantorOffer:
    def __init__(self):
        self.currencies = []

    def load_offer(self):
        self.currencies.append(Currency('EUR', 'Euro', 'Euro.jpg'))
        self.currencies.append(Currency('USD', 'Dollar', 'USD.jpg'))
        self.currencies.append(Currency('GBP', 'British Pound', 'GBP.jpg'))

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknown', 'unknown', 'ban.png')

def main():
    app.run()


@app.route('/')
def index():
    print(request.query_string)

    color = 'black'
    if 'color' in request.args:
        color = request.args['color']

    style = 'normal'
    if 'style' in request.args:
        style = request.args['style']

    time_now = datetime.now().strftime('%H:%M:%S')
    return f'<h1 Style = "color: {color}; font style: {style};"> Hello World! <br /> It\'s:{time_now}</h1>'


@app.route('/links')
def links():
    body = '''<a href='https://www.google.com' target="_blank">Google</a> <br />
    It's the website of Google</a>'''
    return body


@app.route('/cantor/<string:currency>/<int:amount>')
def cantor(currency, amount):
    message = f'<h1>You selected {currency} and {amount}</h1>'
    return message


@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    offer = CantorOffer()
    offer.load_offer()

    if request.method == 'GET':
        return render_template('exchange.html', offer=offer)
    else:
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']

        return render_template('exchange_result.html', currency=currency, amount=amount, currency_info=offer.get_by_code(currency))
    # body = '''
    # <form id="exchange_form" action="/exchange_process" method='POST'>
    # <label for="currency">Currency
    # '''


@app.route('/about')
def about():
    return '<h1> Python flask app<h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Welcome {}!</h1>'.format(name)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
