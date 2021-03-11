import flask
import subprocess
from forms import LoginForm
from netmiko import ConnectHandler

app = flask.Flask(__name__)
app.secret_key = '\x8f\xc7<$<\xbc\x9b\x0b\xc1\xa5o\x15+t\x98w'

@app.route('/')
def samplefunction():
    s = flask.session.get('login')
    if s == None:
        return flask.redirect('/login')
    return flask.render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = {'username': form.username.data, 'password': form.password.data, 'ip_address': form.ip_address.data}
        flask.session['login'] = data
        return flask.redirect('/')
    return flask.render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    flask.session.pop('login')
    return flask.redirect('/login')


@app.route('/lab01')
def lab01():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_01_revised.py | python3")
    return f'''
        <html>
            <body>
            <p> <pre>{output}</pre> </p>
            </body>
        </html>
    '''


@app.route('/lab02')
def lab02():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_02_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab03')
def lab03():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_03_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab04')
def lab04():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_04_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab05')
def lab05():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_05_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab06')
def lab06():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_06_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab07')
def lab07():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_07_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab08')
def lab08():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_08_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab09')
def lab09():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_09_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab10')
def lab10():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password'],
           'secret': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    net_connect.enable()
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_10_rewrite.py | sudo python3")
    net_connect.exit_enable_mode()

    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab11')
def lab11():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_11_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab12')
def lab12():
    s = flask.session.get('login')
    #    def inner():
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_12_test.py | python3")
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''

@app.errorhandler(netmiko.ssh_exception.NetmikoAuthenticationException)
def login_error():
    return 'Incorrect Password. Logout and try again.'
