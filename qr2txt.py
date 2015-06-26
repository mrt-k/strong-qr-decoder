#!/usr/bin/env python2
#-*- codinf: utf-8 -*-

import pyqrcode
import sys
from PIL import Image 
import argparse

parser = argparse.ArgumentParser(description='QR code to text')
parser.add_argument('-f', '--file', required=True, help='QR code File')
args = parser.parse_args()


im = Image.open(args.file)
#print im.size

px = im.getdata()
for i in range(len(px)):
    if i%im.size[0] == 0:
        print ''
    if px[i] == 255:
        sys.stdout.write('_')
    else:
        sys.stdout.write('X')
