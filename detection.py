from hc_sr04 import *
from StdServo import *
import time
from HCI import *

def front_detect( FRONT_TRIGGER, FRONT_ECHO, IsOpen ):
		distance = get_distance( FRONT_TRIGGER, FRONT_ECHO, 70 )
		#print distance
		if distance <= 50 and IsOpen[0] == False:
			lid_open( 5 )
			IsOpen[0] = True
		elif distance > 50 and IsOpen[0] == True:
			time.sleep( 3 )
			IsOpen[0] = False
		elif distance > 50 and IsOpen[0] == False:
			lid_close( 5 )
			IsOpen[0] = False
		#time.sleep(0.5)

def inside_detect( IR_SENSOR_0, IR_SENSOR_1, IR_SENSOR_2, IR_SENSOR_3 ):
	IR_SENSOR_0_status = GPIO.input( IR_SENSOR_0 )
	IR_SENSOR_1_status = GPIO.input( IR_SENSOR_1 )
	IR_SENSOR_2_status = GPIO.input( IR_SENSOR_2 )
	IR_SENSOR_3_status = GPIO.input( IR_SENSOR_3 )
	
	if IR_SENSOR_0_status and IR_SENSOR_1_status and IR_SENSOR_2_status and IR_SENSOR_3_status:
		return "I am hungry"
	elif (not IR_SENSOR_0_status) and IR_SENSOR_1_status:
		return "feed me more"
	elif not IR_SENSOR_1_status and IR_SENSOR_2_status and IR_SENSOR_3_status:
		return "almost full"
	elif not IR_SENSOR_2_status or not IR_SENSOR_3_status:
		return "full"
