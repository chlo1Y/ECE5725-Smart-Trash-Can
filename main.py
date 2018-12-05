import RPi.GPIO as GPIO
import time
from hc_sr04 import *
from StdServo import *
from StdServo import *
import pygame
from HCI import *
import os # for OS calls
from detection import *
from constants import *
from check_time import *
from check_internet_connection import *
from multiprocessing import Process, Queue
from email_reminder import *
from voice_cmd import *



# ultrasonic setup
GPIO.setmode( GPIO.BCM )
GPIO.setup( FRONT_TRIGGER, GPIO.OUT )
GPIO.setup( FRONT_ECHO, GPIO.IN )

# Bail out button
GPIO.setup( 23,GPIO.IN,pull_up_down=GPIO.PUD_UP ) 

# IR setup
GPIO.setup( IR_SENSOR_0, GPIO.IN, pull_up_down=GPIO.PUD_UP )
GPIO.setup( IR_SENSOR_1, GPIO.IN, pull_up_down=GPIO.PUD_UP )
GPIO.setup( IR_SENSOR_2, GPIO.IN, pull_up_down=GPIO.PUD_UP )
GPIO.setup( IR_SENSOR_3, GPIO.IN, pull_up_down=GPIO.PUD_UP )

# StdServo setup
GPIO.setup( 5, GPIO.OUT )

# pygame initialization
os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
pygame.mouse.set_visible(False)
size = width, height = 320, 240
screen = pygame.display.set_mode( size )
my_font = pygame.font.Font( None,20 )

GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
	while True:
		# check if bail out button is pushed
	 	bail_out = GPIO.input(23)
	 	if not bail_out:
			break

		# check whether the trash is commanded by voice or ultrasonic sensor
		if IsVoiceMode[0] == False:
			front_detect( FRONT_TRIGGER, FRONT_ECHO, IsOpen )
		
		# detect inside status of trash can and draw accordingly
		inside_status = inside_detect( IR_SENSOR_0, IR_SENSOR_1, IR_SENSOR_2, IR_SENSOR_3 )
		draw( inside_status, screen, my_font )
		
		# detect voice command
		voice_cmd_bridge( IsOpen, IsVoiceMode, LastVoiceCmd )
		
		# check time, only send reminder email when trash can is full
		# and it is the end of the day
		IsEndOfDay[0] = check_time( "23", "59" )
		IsBeginOfDay[0] = check_time( "00", "00" )
		if IsEndOfDay[0] and not DailyReminderSent[0] and inside_status == "full":
			if( check_internet() ):
				send_reminder_email()
				DailyReminderSent[0] = True
			else:
				print "your are disconnected, i can not send you a remidner email, please check your connection" 
		elif IsBeginOfDay[0]:
			DailyReminderSent[0] = False
		
		# set polling frequency to 2hz
		time.sleep( 0.5 )

except KeyboardInterrupt:
	pass

lid_close( 5 )
GPIO.cleanup()
pygame.quit()
print "done!"
