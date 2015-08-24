from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/course/<course_id>')
def course_info(course_id):
    return render_template('course_description.html')

@app.route('/course/<course_id>/info/<question_id>')
def question_info(course_id, question_id):
	print 'here'
	return render_template('question_info.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')