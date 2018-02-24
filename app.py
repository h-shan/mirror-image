from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response
app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__)
import text_analytics
import luis_request

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
	user_input = request.form['input']
	
	resp = make_response(redirect(url_for('result')))
	resp.set_cookie("input", user_input)
	return resp

@app.route('/result/')
def result():
	user_input = request.cookies.get('input')

	#score, subjects = text_analytics.analyze(user_input)
	luis_res = luis_request.request_luis(user_input)

	return render_template('result.html', luis=luis_res)#score=score, subjects=subjects, luis=luis_res)

if __name__ == "__main__":
	app.run(debug=True, threaded=True)