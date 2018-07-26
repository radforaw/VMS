import requests
try:
  from lxml import etree as ET
except ImportError:
  import xml.etree.cElementTree as ET
import datetime
import time

url='http://bcc.opendata.onl/UTMC VMS.xml'
n=requests.get(url,params={'ApiKey':'7N0BRC3CT4KIB4BY5342743137151'})
root=ET.fromstring(n.content)
print n.content
