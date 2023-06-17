from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World2!</h1>"
    #https://red-analyst-pyobu.pwskills.app:5000/hello_world2 

@app.route("/test")
def test() :
    a = 865+765
    return "this is my function to run app {}".format(a)
    #https://red-analyst-pyobu.pwskills.app:5000/test 

@app.route("/test2/test2")
def test2() :
    data = request.args.get('x')
    return "this is a data input from my url {}".format(data)
    #https://red-analyst-pyobu.pwskills.app:5000/test2/test2?x=priy

if __name__=="__main__":
    app.run(host="0.0.0.0")
