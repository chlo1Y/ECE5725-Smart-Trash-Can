# this is stdard servo function module

import RPi.GPIO as GPIO
import time


def lid_open( SERVO_IO ):
	pulse_width = 0.75;
	freq = 1000 / ( pulse_width + 20 ) 
	dc = 100*pulse_width / ( 20 + pulse_width )
	pwm = GPIO.PWM( SERVO_IO, freq )
	pwm.start(dc)
	time.sleep( 0.5 )
	pwm.stop()

def lid_close( SERVO_IO ):
	pulse_width = 2
	freq = 1000 / ( pulse_width + 20 ) 
	dc = 100*pulse_width / ( 20 + pulse_width )
	pwm = GPIO.PWM( SERVO_IO, freq )
	pwm.start(dc)
	time.sleep( 0.5 )
	pwm.stop()
