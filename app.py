from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'world'

@app.route('/Chicago/<name>')
def show_name(name):
    return 'Chicago ' +name

@app.route('/Ashish/<last_name>')
def name(last_name):
    return 'Ashish ' +last_name


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')