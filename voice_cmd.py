# this is voice commad reading module
# read from voice recognition output 
# and decide open trash can or not

from StdServo import *
import time 
import RPi.GPIO as GPIO

def voice_cmd_bridge( IsOpen, IsVoiceMode, LastVoiceCmd ):
	cmd_file = open( "voice_command.txt", "r" )
	cmd = str(cmd_file.read())
	cmd_file.close()
	#print cmd
	if LastVoiceCmd[0] != cmd:
		if cmd == "close" and IsOpen[0] == True:
			#print "about to close"
			lid_close( 5 )
			IsOpen[0] = False
			IsVoiceMode[0] = False
			LastVoiceCmd[0] = "close"
			#cmd_file = open( "voice_command.txt", "w" )
			#cmd_file.write("clear")
			#cmd_file.close()
			#cmd_file.write("clear")
		elif cmd == "open" and IsOpen[0] == False:
			#print "about to open"
			lid_open( 5 )
			IsOpen[0] = True
			IsVoiceMode[0] = True
			LastVoiceCmd[0] = "open"
			#cmd_file = open( "voice_command.txt", "w" )
			#cmd_file.write("clear")
			#cmd_file.close()
			#cmd_file.write("clear")



if __name__ == "__main__":
	'''
	GPIO.setmode( GPIO.BCM )
	GPIO.setup( 5, GPIO.OUT )
	voice_cmd_bridge( [True] )
	GPIO.cleanup()
	'''

	try:
		while True:
			cmd_file = open( "voice_command.txt", "r" )
			cmd = str(cmd_file.read())
			cmd_file.close()
			print cmd
			time.sleep(0.5)
	except KeyboardInterrupt:
		pass

	
