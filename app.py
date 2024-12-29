from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return "Hello World!"
    
@app.route('/page1')
def page1():
    return "Hello World from Page1"

@app.route('/page2')
def page2():
    return "Hello World from Page2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
