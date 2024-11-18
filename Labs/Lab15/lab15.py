#Import library
import urllib.request, urllib.parse, urllib.error
import json

#Read data from URL
url = 'http://py4e-data.dr-chuck.net/comments_1430672.json'
data = urllib.request.urlopen(url).read()
#Convert to dict
js = json.loads(data)

total = 0
#iterate through the list (1 line is 1 dictionary)
for item in js['comments']:
    total += int(item['count'])
print('Có tổng cộng {} comment'.format(total))