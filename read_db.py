import sqlite3
conn = sqlite3.connect('networks.db')
c = conn.cursor()

t=('vsrx2',)
c.execute('SELECT * FROM devices WHERE hostname=?', t)
print(c.fetchone())
print('aaaaaaaaaa')
print('aaaaaaaaaa')
hosts = c.execute('SELECT * FROM devices ORDER BY hostname')
for i in hosts:
    print(i)

