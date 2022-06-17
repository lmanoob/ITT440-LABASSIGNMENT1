from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.50.164',  #Your Server IP
    'username': 'lmao', #your Server Username
    'password': 'lmao', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)
