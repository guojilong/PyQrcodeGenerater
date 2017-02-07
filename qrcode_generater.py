#!/usr/bin/env  python
#coding=utf-8
import qrcode
from PIL import Image
import os



def generateQrcode(content,path):
	qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
	)
	qr.add_data(content)
	qr.make(fit=True)
	img = qr.make_image()
	path=os.path.expanduser(path)
	if os.path.exists(path):
		os.remove(path)

	img.save(os.path.expanduser(path))



for channl in range(4001,4011):
	url='http://www.ishansong.com/static/pc/down-ssy.html?channel=%s' % channl
	path='~/Desktop/qrcode/%s.png' % channl

	generateQrcode(url,path)
	 


