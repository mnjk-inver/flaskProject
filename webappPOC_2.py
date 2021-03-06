import flask
import subprocess
from forms import LoginForm
#from flask_session import Session
#from flask import render_template, session, request
from netmiko import ConnectHandler

app = flask.Flask(__name__)
app.secret_key = 'super secret key'
#app.config['SESSION_TYPE'] = 'filesystem'
#Session(app)

@app.route('/')
def samplefunction():
    s = flask.session.get('login')
    print(s)
    return flask.render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = {'username': form.username.data, 'password': form.password.data, 'ip_address': form.ip_address.data}
        flask.session['login'] = data
        return flask.redirect('/')
    return flask.render_template('login.html', title='Sign In', form=form)

@app.route('/lab01')
def lab01():
    s = flask.session.get('login')
#    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_01_revised.py | python3",
    # proc = subprocess.Popen(
    #     ['python3 lab_01_remote.py'],
    #     shell=True,
    #     stdout=subprocess.PIPE,
    #     universal_newlines=True
        )
    return f'''
        <html>
            <body>
            <p> <pre>{output}</pre> </p>
            </body>
        </html>
    '''
 #   return flask.Response(inner(), mimetype='text/html')

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
