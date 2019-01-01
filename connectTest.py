#!/usr/bin/env python

from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler

lax_tar_r1 = {
	'device_type':'juniper',
	'ip':'127.0.0.1',
    'port':'22221',
	'username':'akif',
	'password':'Akif999',
	'verbose':True,
}

# Connect to device with given arguments in lax_tar_r1
net_connect = ConnectHandler(**lax_tar_r1)

net_connect.enable()
config_commands = [
	'set system host-name vsrx1',
    'commit',
]

output = net_connect.send_config_set(config_commands)
print(output)

