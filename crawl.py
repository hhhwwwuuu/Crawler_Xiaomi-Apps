#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
#import cookielib
import urllib.request
import re
import sys
from urllib.request import urlretrieve
import spider
#import requests

#reload(sys)
#sys.setdefaultencoding("utf-8")




url = "http://app.mi.com/download/62289?id=com.xiaomi.o2o&ref=appstore.mobile_download&nonce=-553189008766792780%3A25943398&appClientId=2882303761517485445&appSignature=gmmJ_uC754lfFN_2Smb-GvUMPjg724AWAu7IMLBmdlU"
#response1 = urllib.request.urlopen(url)
#result = response1.read().decode('UTF-8')
#urlretrieve(url, './apps/xiaomi')
category = {}
if __name__ == '__main__':
	url = "http://app.mi.com"
	crawler = spider.Spider(url)
	result = crawler.getSubpage()
	print(result)
	#if spider.downloadApp(url,'xiaomi', 'shopping'):
	#	print("finished!")
	#else:
	#	print("Failed!")