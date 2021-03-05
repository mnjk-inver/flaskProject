import flask
import subprocess
import time

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def samplefunction():
    return flask.render_template('index.html')

@app.route('/lab01')
def lab01():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_remote.py'],
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')

@app.route('/lab02')
def lab02():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab03')
def lab03():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab04')
def lab04():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab05')
def lab05():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab06')
def lab06():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab07')
def lab07():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab08')
def lab08():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab09')
def lab09():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab10')
def lab10():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab11')
def lab11():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

@app.route('/lab12')
def lab12():
    def inner():
        proc = subprocess.Popen(
            ['python3 lab_01_revised.py'],  # call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            yield line + "<br/>\n"

        # for line in iter(proc.stdout.readline, ''):
        #      yield line

    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$


#     return render_template('lab01.html',output=lab_01_revised)

# app.run(debug=True, port=5000, host='0.0.0.0')
