from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def hello_world():
    user_agent = request.headers.get('User_Agent')
    print(user_agent)
    return 'Hello World!,your agent is %s' %user_agent


@app.route('/user/<path:id>')
def user(id):
    return '<h1>Hello,%s...</h1>' %id


if __name__ == '__main__':

    #print(__name__)
    app.run(debug=True)
