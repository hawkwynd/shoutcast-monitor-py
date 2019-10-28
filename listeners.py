#!/usr/bin/python
import urllib2
import json
import config

url = config.sc['host']+config.sc['port']+config.sc['path']+config.sc['sid']+config.sc['mode']+config.sc['passw']

results = urllib2.urlopen(url).read()
data  = json.loads(results)

print ("\nHawkwynd Radio Current listeners")
print ("--------------------------------\n")

for i in data['listeners']:
    
    hostname = i['hostname']
    locUrl = "http://ipinfo.io/"+hostname+"/json"
    res = urllib2.urlopen(locUrl).read()  
    pak = json.loads(res)
    
    # calculate time online
    millis = int(i['connecttime']*1000)
    seconds = (millis/1000)%60
    seconds = int(seconds)
    minutes = (millis/(1000*60))%60
    minutes = int(minutes)
    hours = (millis/(1000*60*60))%24
   
    if pak['region'] == '':
        pak['region']='Unknown Region'

    print (pak['ip'] + "\t" + pak['city'] , pak['region'] +", " + pak['country'] + " connected: " + ("%d:%d:%d" % (hours, minutes, seconds)) )
    

print ("\n")

