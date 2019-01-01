import sqlite3

conn = sqlite3.connect('networks.db')
c = conn.cursor()
c.execute('''CREATE TABLE devices (hostname text, attributes text)''')

c.execute('''INSERT INTO devices VALUES( 'vsrx1', "{ 'device_type': 'juniper', 'ip': '127.0.0.1', 'port': '22221', 'username': 'akif', 'password': 'Akif999' }")''')
c.execute('''INSERT INTO devices VALUES( 'vsrx2', "{ 'device_type': 'juniper', 'ip': '127.0.0.1', 'port': '22222', 'username': 'akif', 'password': 'Akif999' }")''')
c.execute('''INSERT INTO devices VALUES( 'vsrx3', "{ 'device_type': 'juniper', 'ip': '127.0.0.1', 'port': '22223', 'username': 'akif', 'password': 'Akif999' }")''')
c.execute('''INSERT INTO devices VALUES( 'vsrx4', "{ 'device_type': 'juniper', 'ip': '127.0.0.1', 'port': '22224', 'username': 'akif', 'password': 'Akif999' }")''')
conn.commit()

t=('vsrx2',)
c.execute('SELECT * FROM devices WHERE hostname=?', t)
print(c.fetchone())
hosts = c.execute('SELECT * FROM devices ORDER BY hostname')
for i in hosts:
    print(i)

