from __future__ import print_function
import sqlite3, ast

conn = sqlite3.connect('networks.db')
c = conn.cursor()

t=('vsrx2',)
c.execute('SELECT * FROM devices WHERE hostname=?', t)
t = c.fetchone()
conn.close()

#print (t[0], t[1])

hostname = t[0]
device_attributes = t[1]

#print(f'Hostname: {hostname}, Attr: {device_attributes}')
print("Hostname: %s, Attr: %s" % (hostname, device_attributes))
print('*' * 10)
attr = ast.literal_eval(device_attributes)  # Converts string to dictionar
print(attr)
