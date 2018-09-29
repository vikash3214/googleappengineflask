from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hellow')
@app.route('/')
def hello():
    return render_template('hellow.html')


if __name__=="__main__":
	app.run()
