from flask import Flask
from flask import render_template
from flask import make_response
import time
app = Flask(__name__)
@app.route("/")
def hello():
	res = make_response(render_template('index.html'))
	res.set_cookie(key='testcookie',value='haha',expires = time.time()+6*60)
	return res
@app.route("/test")
def test():

if __name__ == "__main__":
    app.run(debug=True)
