import pyqrcode
import sys
from PIL import Image 

#image = sys.argv[1]

im = Image.open('./qr.png')
print im.size

px = im.getdata()
for i in range(len(px)):
    if i%im.size[0] == 0:
        print ''
    if px[i] == 0:
        sys.stdout.write('X')
    if px[i] == 255:
        sys.stdout.write('_')

print im.size
