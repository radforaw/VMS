import requests
try:
  from lxml import etree as ET
except ImportError:
  import xml.etree.cElementTree as ETtt
import datetime
import time

def get_vms():
url='http://bcc.opendata.onl/UTMC VMS.xml'
n=requests.get(url,params={'ApiKey':'7N0BRC3CT4KIB4BY5342743137151'})
root=ET.fromstring(n.content)
print n.content
ret=[]
for state in root.findall("VMS_State"):
  for VMS in state.findall("VMS"):
    tmp=datetime.datetime.strptime(VMS.find("Date").text,'%Y-%m-%d %H:%M:%S)
    now=datetime.datetime.now()-datetime.timedelta(days=28)
    if tmp>now and len(VMS.find('SCN').text)<20:
      ret.append(VMS.find('Description').text,VMS.find('MessageID').text,(float(VMS.find('Northing').text),(float(VMS.find('Easting'))))
return ret
