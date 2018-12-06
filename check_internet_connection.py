# this is internet connection checking module
# return True if is connected to internet

import urllib2
import time

def check_internet():
	try:
		header = { "pragma" : "bo-cache" }
		req = urllib2.Request( "http://www.google.com", headers = header )
		response = urllib2.urlopen( req, timeout = 2 )
		print " you are connected "
		return True
	except urllib2.URLError as err:
		print err
		return False

if __name__ == "__main__":
	print check_internet()
