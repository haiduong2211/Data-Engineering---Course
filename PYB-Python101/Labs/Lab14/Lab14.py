import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
xmlf = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1430671.xml").read()

tree = ET.fromstring(xmlf)
countcm = tree.findall('.//count') #This is a list of Element 'count' in xml

total = 0
count = 0

for i in countcm:
    x = int(i.text)
    total += x
    count += 1

print('There are',total,'comments')
print("There are {} comments".format(total))