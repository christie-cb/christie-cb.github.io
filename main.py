from flask import Flask
import flask
from app import freezer

app = Flask(__name__)

@app.route("/")
def home():
    author = "Miss Shoe"
    name = "Christie"
    return flask.render_template('index.html', author=author, name=name)


if __name__=="__main__":
    freezer.freeze()
    app.run(debug=True)
