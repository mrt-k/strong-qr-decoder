import pyqrcode
import sys

data = "sample text"
qr = pyqrcode.create(data)

for i in qr.code:
    for j in i:
        if j == 1:
            sys.stdout.write('X')
        if j == 0:
            sys.stdout.write('_')
    print ''

