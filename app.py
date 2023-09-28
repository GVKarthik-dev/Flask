from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return f'<h1>hi ther {name}<h1>'

def hello():
    return 'welcome'
app.add_url_rule('/','welcome',hello)

if __name__ == '__main__':
    app.run(debug=True)