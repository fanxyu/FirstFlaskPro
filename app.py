from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<path:id>')
def user(id):
    return '<h1>Hello,%s...</h1>' %id


if __name__ == '__main__':

    #print(__name__)
    app.run(debug=True)
