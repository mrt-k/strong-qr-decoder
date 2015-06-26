#!/usr/bin/env python2
#-*- coding: utf-8 -*-
import pyqrcode
import sys
import argparse

parser = argparse.ArgumentParser(description='Create QR Code')
parser.add_argument('-d', '--data', required=True, help=u'埋め込むデータ')
parser.add_argument('-o', '--output', default='output.png', help=u'保存名(PNG形式)')
args = parser.parse_args()


data = args.data
qr = pyqrcode.create(data)

for i in qr.code:
    for j in i:
        if j == 1:
            sys.stdout.write('X')
        if j == 0:
            sys.stdout.write('_')
    print ''

qr.png(args.output)
