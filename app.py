from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here


    return 'Hello World! test3 deneme yegitek'

@app.route('/saldir2')
def hello_world2():  # put application's code here
    return 'Hello World saldir2!'

@app.route('/saldir3')
def hello_world3():  # put application's code here
    return 'Hello World saldir3!'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
