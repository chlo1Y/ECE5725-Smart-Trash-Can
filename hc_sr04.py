import RPi.GPIO as GPIO
import time


def get_distance( TRIGGER, ECHO, threshold ):
	GPIO.output( TRIGGER, True )
	time.sleep(0.00001)
	GPIO.output( TRIGGER, False )
	
	StartTime = time.time()
	StopTime = time.time()
	
	while GPIO.input( ECHO ) == 0:
		StartTime = time.time()

	while GPIO.input( ECHO ) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime
	
	distance = ( TimeElapsed * 34300 ) / 2
	distance = filter( distance ,threshold )
	return distance

def filter( raw_distance, threshold ):
	if( raw_distance > threshold ):
		return threshold
	else:
		return raw_distance
