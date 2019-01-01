from netmiko import ConnectHandler

class Router(object):
    def __init__(self, hostname=None,  device_type='juniper', ip=None, port=None, username='root', password='Root999'):
        self.hostname = hostname
        self.device_type = device_type
        self.ip = ip 
        self.port = port 
        self.username= username
        self.password = password

    def show_interface(self):
        self.net_connect = ConnectHandler(device_type=self.device_type, ip=self.ip, port=self.port, username=self.username, password=self.password)
        output = self.net_connect.send_command('show interfaces terse')
        return output

    def set_hostname(self):
        self.net_connect = ConnectHandler(device_type=self.device_type, ip=self.ip, port=self.port, username=self.username, password=self.password)
        self.net_connect.enable()
            
        command = "set system host-name %s" % (self.hostname)

        # Construct the command to execute
        config_commands = [
            'set system host-name' + ' '  + str(self.hostname),
            'commit',
            'exit',
        ]
        output = self.net_connect.send_config_set(config_commands)
        return output

