from __future__ import print_function
from inventory import devices
from router_object_v2 import Router
from pprint import pprint as pp
import sys

for d in devices:
    for key ,value in d.items():
        print(f"Key is: {key} and Value is: {value}")
        r = Router(hostname=key, **value)    
        
        try:
            output = r.set_hostname()
            print(output)
        except:
            print("Cannot connect to server")
            continue

