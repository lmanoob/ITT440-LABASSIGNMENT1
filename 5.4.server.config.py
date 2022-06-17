from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.50.164',  #Your Server IP
    'username': 'lmao', #your Server Username
    'password': 'lmao', #your server password
    'port' : 22,
    'secret': '',
}

commands = ["logging buffered 100000"]
with ConnectHandler(**myserver) as net_connect:
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

print()
print(output)
print()
