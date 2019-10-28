#!/usr/bin/python
import urllib2
import json
import config
import sys

url = config.sc['host']+config.sc['port']+config.sc['path']+config.sc['sid']+config.sc['mode']+config.sc['passw']

results = urllib2.urlopen(url).read()
data  = json.loads(results)

print("Now Playing: " + data['songtitle'])


if not data['listeners']:
    print (config.sc['station'])
    print ("No listeners")
    sys.exit()

print (config.sc['station'] + " Current listeners\n")


for i in data['listeners']:
    
    hostname = i['hostname']
    locUrl = "http://ipinfo.io/"+hostname+"/json"
    res = urllib2.urlopen(locUrl).read()  
    pak = json.loads(res)
    
    # calculate connected time
    millis = int(i['connecttime']*1000)
    seconds = (millis/1000)%60
    seconds = int(seconds)
    minutes = (millis/(1000*60))%60
    minutes = int(minutes)
    hours = (millis/(1000*60*60))%24
   
    if pak['region'] == '':
        pak['region']='Unknown'

    print pak['ip'] + " | " + pak['city'] , pak['region'] +", " + pak['country'] + " | Time: " + ("%d:%d:%d" % (hours, minutes, seconds))
    
print ("\n")

