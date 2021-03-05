# import library
from netmiko import ConnectHandler
# connection properties described in a dictionary

ip_address = '172.17.50.28'
username = 'mnjk'
password = 'Franske2900'

VMR = {'device_type': "linux",'ip':ip_address, 'username': username, 'password': password}

#initiate connection
net_connect = ConnectHandler(**VMR)
output = net_connect.send_command("curl https://raw.githubusercontent.com/mnjk-inver/Linux-2480-Rebuild/main/lab_01_revised.py | python3")
print (output)