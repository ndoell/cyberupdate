'''
Created on Dec 3, 2016

@author: nicholasdoell
'''
#import requests
#import xmltodict
#import xml.etree.ElementTree as ET
import feedparser
from cyberupdate.StripTags import MLStripper
from collections import deque

cveurl = 'https://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Recent.xml.gz'

certfeeds = {'cert_alerts' : 'https://www.us-cert.gov/nacas/alerts.xml',
'cert_currentactivity' : 'https://www.us-cert.gov/ncas/current-activity.xml',
'cert_vulfeed' : 'https://www.kb.cert.org/vulfeed'}
        

def currentactivity():
    rssfeed = feedparser.parse(certfeeds['cert_currentactivity'])
    CERTFeed = rssfeed["channel"]["title"]
#    print('Feed URL: ' +rssfeed["channel"]["link"])
#    print("")
    rssitems = rssfeed["items"]

    for item in rssitems:
        title = item["title"]
        summary = strip_tags(item["summary"])
        # Splitting at the first period space '. ' to determine the end of the first sentence. 
        shortersum = summary.split(". ",1)[0]
        shortdesc = title, shortersum
        print(shortdesc)
    return(CERTFeed)
    

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()    

#print(currentactivity())  
