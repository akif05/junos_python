import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

username = input("Device username: ")
password = getpass("Device password: ")

try:
    with Device(mode='serial', port='port', user=username, passwd=password) as dev:
        print (dev.facts)
        cu = Config(dev)
        cu.lock()
        cu.load(path='/tmp/config_mx.conf')
        cu.commit()
        cu.unlock()

except Exception as err:
    print (err)
    sys.exit(1)
