# check_time funciton is for real time checking, if current hour and minute 
# are target hour and minute, return True

import datetime
import time

def get_current_time():
	time = str(datetime.datetime.now().time()).split(":")
	time[2] = time[2].split(".")[0]
	return time

def check_time( target_hour, target_minute):
	time = get_current_time()
	if( time[0] == target_hour and time[1] == target_minute ):
		return True
	else:
		return False

if __name__ == "__main__":
	print check_time("19","25")
