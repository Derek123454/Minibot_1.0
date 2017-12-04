# Imports
import webiopi

# Retrieve GPIO lib
webiopi.setDebug()
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #

# Left motor GPIOs
L1=18  # H-Bridge 1
L2=23 # H-Bridge 2
LS=14 # H-Bridge 1,2EN

# Right motor GPIOs
R1=24 # H-Bridge 3
R2=25 # H-Bridge 4
RS=15 # H-Bridge 3,4EN

#Aux Motor A GPIOs
A1=20 #H-Bridge 2-1
A2=21 #H-Bridge 2-2
AS=12 #H-Bridge 2-1,2 EN

#Aux Motor B GPIOs
B1=26 #H-Bridge 2-3
B2=19 #H-Bridge 2-4
BS=16 #H-Bridge 2-3,4 EN

PWM1=13 #First PWM 
# -------------------------------------------------- #
# Convenient PWM Function                            #
# -------------------------------------------------- #
def setup():
	GPIO.setFunction(LS, GPIO.PWM)
	GPIO.setFunction(L1, GPIO.OUT)
	GPIO.setFunction(L2, GPIO.OUT)

	GPIO.setFunction(RS, GPIO.PWM)
	GPIO.setFunction(R1, GPIO.OUT)
	GPIO.setFunction(R2, GPIO.OUT)
	
	GPIO.setFunction(AS, GPIO.PWM)
	GPIO.setFunction(A1, GPIO.OUT)
	GPIO.setFunction(A2, GPIO.OUT)
	
	GPIO.setFunction(BS, GPIO.PWM)
	GPIO.setFunction(B1, GPIO.OUT)
	GPIO.setFunction(B2, GPIO.OUT)
	
	GPIO.setFunction(PWM1, GPIO.OUT)
    # I set it to OUT and not PWM because we don't
    #   want the PWM loop running in the background -
    #   that causes the servo to be twitchy. This writes
    #   the PWM signal once and finishes. This probably
    #   blocks the main thread though.
	

	set_speed(0.9)
	Stop()
# Set the speed of two motors
def set_speed(speed):
	GPIO.pulseRatio(LS, speed)
	GPIO.pulseRatio(RS, speed)
	GPIO.pulseRatio(AS, speed)
	GPIO.pulseRatio(BS, speed)

# -------------------------------------------------- #
# Left Motor Functions                               #
# -------------------------------------------------- #

def left_stop():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)

def left_forward():
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(L2, GPIO.LOW)

def left_backward():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)

# -------------------------------------------------- #
# Right Motor Functions                              #
# -------------------------------------------------- #
def right_stop():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

def right_forward():
    GPIO.output(R1, GPIO.HIGH)
    GPIO.output(R2, GPIO.LOW)

def right_backward():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)
	
# -------------------------------------------------- #
# Aux Motor A Functions                              #
# -------------------------------------------------- #
def auxA_stop():
	GPIO.output(A1, GPIO.LOW)
	GPIO.output(A2, GPIO.LOW)
	
def auxA_forward():
	GPIO.output(A1, GPIO.HIGH)
	GPIO.output(A2, GPIO.LOW)
	
def auxA_backward():
	GPIO.output(A1, GPIO.LOW)
	GPIO.output(A2, GPIO.HIGH)
	
# -------------------------------------------------- #
# Aux Motor B Functions                              #
# -------------------------------------------------- #
def auxB_stop():
	GPIO.output(B1, GPIO.LOW)
	GPIO.output(B2, GPIO.LOW)
	
def auxB_forward():
	GPIO.output(B1, GPIO.HIGH)
	GPIO.output(B2, GPIO.LOW)
	
def auxB_backward():
	GPIO.output(B1, GPIO.LOW)
	GPIO.output(B2, GPIO.HIGH)
	
	

# -------------------------------------------------- #
# Macro definition part                              #
# -------------------------------------------------- #

def goforward():
    left_forward()
    right_forward()

def gobackward():
    left_backward()
    right_backward()

def turnleft():
    left_backward()
    right_forward()

def turnright():
    left_forward()
    right_backward()

def Stop():
    left_stop()
    right_stop()
	
	
def auxAforward():
	auxA_forward()
	
def auxAbackward():
	auxA_backward()
	
def auxBforward():
	auxB_forward()
	
def auxBbackward():
	auxB_backward()
	
def auxstop():
	auxB_stop()
	auxA_stop()

def setServo45():
    GPIO.pulseMicroRatio(PWM1, 20000, 0.05) # 1ms HIGH

def setServo0():
    GPIO.pulseMicroRatio(PWM1, 20000, 0.10) # 2ms HIGH

# -------------------------------------------------- #
# Initialization part                                #
# -------------------------------------------------- #

# Setup GPIOs


# -------------------------------------------------- #
# Main server part                                   #
# -------------------------------------------------- #




@webiopi.macro
def go_forward():
	goforward()

@webiopi.macro
def go_backward():
	gobackward()

@webiopi.macro	
def turn_left():
	turnleft()
	
@webiopi.macro	
def turn_right():
	turnright()
	
@webiopi.macro	
def stop():
	Stop()
	
@webiopi.macro
def AuxAforward():
	auxAforward()
	
@webiopi.macro
def AuxAbackward():
	auxAbackward()
	
@webiopi.macro
def AuxBforward():
	auxBforward()
	
@webiopi.macro
def AuxBbackward():
	auxBbackward()
	
@webiopi.macro
def Auxstop():
	auxstop()
	
@webiopi.macro
def set_servo_0():
    setServo0()

@webiopi.macro
def set_servo_45():
    setServo45()

