from flask import Flask, render_template
from flask import request
from flask import abort, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return "contact with me"

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505

@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/about')
def about():
    return app.send_static_file('about.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
