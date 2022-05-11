from pydoc import render_doc
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_templete('hello.html')

if __name__ == '__main__':
    app.run()