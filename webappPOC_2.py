import flask
import subprocess
from forms import LoginForm
from netmiko import ConnectHandler
import netmiko, time

#set flask application to variable app
app = flask.Flask(__name__)
#secret key used to encrypt cookie for session
app.secret_key = '\x8f\xc7<$<\xbc\x9b\x0b\xc1\xa5o\x15+t\x98w'

#link to index page
@app.route('/')
def samplefunction():
#check for existence of session
    s = flask.session.get('login')
#if no session go to login screen
    if s == None:
        return flask.redirect('/login')
    #if session, present index.html
    return flask.render_template('index.html')

1
@app.route('/login', methods=['GET', 'POST'])
def login():
#call form for inputting login info
    form = LoginForm()
    if form.validate_on_submit():
        data = {'username': form.username.data, 'password': form.password.data, 'ip_address': form.ip_address.data}
        #store login info in a session cookie
        flask.session['login'] = data
        #check if ip address is on 172.17.50.xx subnet
        if "172.17.50." not in data['ip_address']:
            #if not delete session
            flask.session.pop('login')
            #display error message
            flask.flash( "You may only use this software to log into a 172.17.50.xx address")
            #return to login screen
            return flask.redirect('/login')
        # return to index page
        return flask.redirect('/')
    return flask.render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    #delete session info
    flask.session.pop('login')
    return flask.redirect('/login')


@app.route('/lab01')
def lab01():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    #run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_01_revised.py | python3")
    #display command output
    return f'''
        <html>
            <body>
            <p> <pre>{output}</pre> </p>
            </body>
        </html>
    '''


@app.route('/lab02')
def lab02():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_02_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab03')
def lab03():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_03_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab04')
def lab04():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_04_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab05')
def lab05():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_05_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab06')
def lab06():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_06_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab07')
def lab07():
    #check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_07_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab08')
def lab08():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_08_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab09')
def lab09():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_09_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab10')
def lab10():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password'],
           'secret': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    #enable sudo on remote host
    net_connect.enable()
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_10_rewrite.py | sudo python3")
    net_connect.exit_enable_mode()
    # display command output

    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab11')
def lab11():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_11_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''


@app.route('/lab12')
def lab12():
    # check for existence of session
    s = flask.session.get('login')
    #    set login info from session as dictionary
    VMR = {'device_type': "linux", 'ip': s['ip_address'], 'username': s['username'], 'password': s['password']}

    # initiate connection
    net_connect = ConnectHandler(**VMR)
    # run command on remote host
    output = net_connect.send_command(
        "curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_12_test.py | python3")
    # display command output
    return f'''
            <html>
                <body>
                <p> <pre>{output}</pre> </p>
                </body>
            </html>
        '''

#check for netmiko authentication error
@app.errorhandler(netmiko.ssh_exception.NetmikoAuthenticationException)
def login_error(test):
    return 'Incorrect Password. Logout and try again.'
