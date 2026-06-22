from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/saldir2')
def hello_world():  # put application's code here
    return 'Hello World saldir2!'


if __name__ == '__main__':
    app.run()
