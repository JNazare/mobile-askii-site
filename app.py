from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/course/<course_id>')
def course_info(course_id):
    return render_template('course_description.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')