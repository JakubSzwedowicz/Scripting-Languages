from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


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


@app.route('/exhange')
def exchange():
    body = '''
    <form id="exchange_form" action="/exchange_process" method='POST'>
    <label for="currency">Currency
    '''


@app.route('/about')
def about():
    return '<h1> Python flask app<h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Welcome {}!</h1>'.format(name)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
