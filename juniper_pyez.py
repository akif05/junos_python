# pip install ncclient
# pip install lxml
# pip install junos-eznc

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

routers = ['127.0.0.1']

pyez_user = 'akif'
pyez_pass = 'Akif999'
pyez_port = '22221'

for router in routers:
    device = Device(host=router, user=pyez_user, password=pyez_pass, port=pyez_port)
    device.open()
    print(device.facts)
    device.close()

# To do configuration on juniper box

dev = Device(host='127.0.0.1', user='akif', password='Akif999', port='22222')
dev.open()
with Config(dev, mode='private') as cu:
    cu.load('set system services netconf traceoptions file test.log', format='set')
    cu.pdiff()
    cu.commit()
dev.close()
# {'2RE': False, 'HOME': '/var/home/akif', 'RE0': None, 'RE1': None, 'RE_hw_mi': False, 'current_re': ['master', 'node', 'fwdd', 'member', 'pfem', 're0', 'fpc0', 'localre'], 'domain': 'entry', 'fqdn': 'vsrx1.entry', 'hostname': 'vsrx1', 'hostname_info': {'fpc0': 'vsrx1'}, 'ifd_style': 'CLASSIC', 'junos_info': {'fpc0': {'text': '17.4R1.16', 'object': junos.version_info(major=(17, 4), type=R, minor=1, build=16)}}, 'master': None, 'model': 'VQFX-10000', 'model_info': {'fpc0': 'VQFX-10000'}, 'personality': None, 're_info': None, 're_master': None, 'serialnumber': '130178338920', 'srx_cluster': None, 'srx_cluster_id': None, 'srx_cluster_redundancy_group': None, 'switch_style': 'VLAN_L2NG', 'vc_capable': True, 'vc_fabric': False, 'vc_master': '0', 'vc_mode': 'Enabled', 'version': '17.4R1.16', 'version_RE0': None, 'version_RE1': None, 'version_info': junos.version_info(major=(17, 4), type=R, minor=1, build=16), 'virtual': None}
