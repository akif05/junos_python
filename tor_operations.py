from __future__ import print_function
from tor_inventory import devices
from router_object_v2 import Router
import sys

#print("Loop thru all devices")
#for d in devices:
#    for key, value in d.items():
#        print(key, d[key])

#print("This is the first device in inventory: " + str(devices[0]))
#router = devices[0]

for d in devices:
    for key ,value in d.items():

        print("Key is the hostname: " + key)
        r = Router(hostname=key, **value)    
        
        #output = r.set_hostname()
        #print(output)

        output = r.show_interface()
        print(output)
        sys.exit()
