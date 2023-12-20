import timeit
import datetime
import json
import decimal
import pyodbc
import time, sys

t = datetime.datetime.now()
print(t.strftime('%Y%m%dT%H%M%S.sss'))
exit(0)

conn_str = 'DRIVER=ms-sql;SERVER=192.168.1.150;PORT=59801;DATABASE=MarketData;TDS_VERSION=8.0;UID=test_user;PWD=peterzhang;'
print('Test login')
conn = None
try:
    conn = pyodbc.connect(conn_str, autocommit=True, timeout=5)
    conn.timeout = 5
    print(conn)
except Exception as e:
    print(e)
    exit(-1)
print('Login is successful.')

print('Sleep')
time.sleep(30)

print('Test execution')
try:
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 1 * FROM MarketData.dbo.trade_dates')
except Exception as e:
    print(e)
exit()

class Test(object):
    def __init__(self):
        self.a = 1
        self.b = 'b'

    def to_str(self):
        return '1'

class ExtendedJSONEncoder(object):
    @staticmethod
    def encoder(obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime.datetime):
            return "%s" % obj
        else:
            return obj.__dict__

a = 3.3
b = decimal.Decimal(3.3)
c = Test()
print(type(a))
print(type(b))

val = {'a': a, 'b': 'aaaaaa'}
print(json.dumps(val))
val = {'a': a, 'b': b, 'c': c, 'd': [1, 2, 3], 'e': (1, 2, 3)}
print(json.dumps(val, default=ExtendedJSONEncoder.encoder))

print('string is object: %s' % (isinstance("a", object)))