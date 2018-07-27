import requests
try:
	from lxml import etree as ET
except ImportError:
	import xml.etree.cElementTree as ET
import datetime
import time
import os
import config

def get_vms():
	url='http://bcc.opendata.onl/UTMC VMS.xml'
	n=requests.get(url,params={'ApiKey':os.environ['ALKEY']})
	root=ET.fromstring(n.content)
	ret=[]
	#print root('VMS_State')
	for VMS in root.iterfind('VMS'):
		tmp=datetime.datetime.strptime(VMS.find("Date").text,'%Y-%m-%d %H:%M:%S')
		now=datetime.datetime.now()-datetime.timedelta(days=28)
		if tmp>now and len(VMS.find('SCN').text)<20 and VMS.find('Message').text:
			ret.append([VMS.find('Description').text,VMS.find('Message').text,(float(VMS.find('Northing').text),(float(VMS.find('Easting').text)))])
	return ret

for b in get_vms():
	print b[0]
	print b[2]
	print b[1].replace('|','\n')
	print
