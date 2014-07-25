#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")
data_all = json.load(htmltext)
data = data_all['data']

print "'MEM_NUM   age    job    MEM_CODE    etc'"
for element in data:
	print "%5s %7s %12s %15s" % (element['MEM_NUM'], element['age'], element['job'], element['MEM_CODE']),
	if element['age'] > 50:
		print ' %8s' % 'Old'
	else:
		print

