from flask import render_template, Flask, request
from apps import app

#app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
	return render_template("xiurista.html")

#if __name__ == "__main__":
#	app.run(port = 5000)