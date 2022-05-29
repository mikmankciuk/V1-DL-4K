import pygame
import time
import RPi.GPIO as GPIO
from time import sleep

giveup = 0

sleep(15)

if not giveup:
    try:
        # Initialise the pygame library
        pygame.init()
        # Connect to the first JoyStick
        j = pygame.joystick.Joystick(0)
        j.init()

        print ('Initialized Joystick : %s' % j.get_name())
        
    except:
        print("Cant find a controller")
#
        
GPIO.setmode(GPIO.BOARD) # BOARD - piny jak na plytce | BCM - piny jak na GPIOx
GPIO.setwarnings(False)

# przygotowanie pinow

GPIO.setup(12, GPIO.OUT) # pwm1
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(32, GPIO.OUT) #pwm2
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

GPIO.setup(33, GPIO.OUT) #pwm3
GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

GPIO.setup(35, GPIO.OUT) #pwm4
GPIO.setup(37, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

#jak toglowac
# GPIO.output(18, not GPIO.input(18))

pi_pwm1 = GPIO.PWM(12, 1000)
pi_pwm2 = GPIO.PWM(32, 1000)
pi_pwm3 = GPIO.PWM(33, 1000)
pi_pwm4 = GPIO.PWM(35, 1000)

pi_pwm1.start(0)
pi_pwm2.start(0)
pi_pwm3.start(0)
pi_pwm4.start(0)

def updateEngine(ID,forward,backward,speed):
    if speed > 100:
        speed = 100
    if speed < -100:
        speed = -100
    
    #
    # forward = 1 backward = 0 => do przodu
    #
    # 0 1 => do tylu
    #
    # 0 0 => 'soft stop'
    #
    # 1 1 => tylko zmiana predkosci
    #
    # WAZNE predkosc z zakresu 0 - 100 [%]
    #
    # pwm wypelniane %
    # pi_pwm1.ChangeDutyCycle(speed)
    #
    if ID == 1:
        if forward == 1 and backward == 0:
            if speed >= 0:
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(16, GPIO.LOW)
                pi_pwm1.ChangeDutyCycle(speed)
                return
            else:
                GPIO.output(18, GPIO.LOW)
                GPIO.output(16, GPIO.HIGH)
                pi_pwm1.ChangeDutyCycle(-speed)
                return
        if forward == 0 and backward == 1:
            if speed >= 0:
                GPIO.output(18, GPIO.LOW)
                GPIO.output(16, GPIO.HIGH)
                pi_pwm1.ChangeDutyCycle(speed)
                return
            else:
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(16, GPIO.LOW)
                pi_pwm1.ChangeDutyCycle(-speed)
                return
        if forward == 0 and backward == 0:
            GPIO.output(18, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
        if forward == 1 and backward == 1:
            if speed >= 0:
                pi_pwm1.ChangeDutyCycle(speed)
            else:
                pi_pwm1.ChangeDutyCycle(-speed)
    if ID == 2:        
        if forward == 1 and backward == 0:
            if speed >= 0:
                GPIO.output(38, GPIO.HIGH)
                GPIO.output(36, GPIO.LOW)
                pi_pwm2.ChangeDutyCycle(speed)
                return
            else:
                GPIO.output(38, GPIO.LOW)
                GPIO.output(36, GPIO.HIGH)
                pi_pwm2.ChangeDutyCycle(-speed)
                return
        if forward == 0 and backward == 1:
            if speed >= 0:
                GPIO.output(38, GPIO.LOW)
                GPIO.output(36, GPIO.HIGH)
                pi_pwm2.ChangeDutyCycle(speed)
                return
            else:
                GPIO.output(38, GPIO.HIGH)
                GPIO.output(36, GPIO.LOW)
                pi_pwm2.ChangeDutyCycle(-speed)
                return
        if forward == 0 and backward == 0:
            GPIO.output(38, GPIO.LOW)
            GPIO.output(36, GPIO.LOW)
        if forward == 1 and backward == 1:
            if speed >= 0:
                pi_pwm2.ChangeDutyCycle(speed)
            else:
                pi_pwm2.ChangeDutyCycle(-speed)
                
    if ID == 3:
        if forward == 1 and backward == 0:
            if speed >= 0:
                GPIO.output(29, GPIO.HIGH)
                GPIO.output(31, GPIO.LOW)
                pi_pwm3.ChangeDutyCycle(speed)
                return
            else:
                GPIO.output(29, GPIO.LOW)
                GPIO.output(31, GPIO.HIGH)
                pi_pwm3.ChangeDutyCycle(-speed)
                return
        if forward == 0 and backward == 1:
            if speed >= 0:
                GPIO.output(29, GPIO.LOW)
                GPIO.output(31, GPIO.HIGH)
                pi_pwm3.ChangeDutyCycle(speed)
                return
            else:
                GPIO.output(29, GPIO.HIGH)
                GPIO.output(31, GPIO.LOW)
                pi_pwm3.ChangeDutyCycle(-speed)
                return
        if forward == 0 and backward == 0:
            GPIO.output(29, GPIO.LOW)
            GPIO.output(31, GPIO.LOW)
        if forward == 1 and backward == 1:
            if speed >= 0:
                pi_pwm3.ChangeDutyCycle(speed)
            else:
                pi_pwm3.ChangeDutyCycle(-speed)
    if ID == 4:
        if forward == 1 and backward == 0:
            if speed >= 0:
                GPIO.output(40, GPIO.HIGH)
                GPIO.output(37, GPIO.LOW)
                pi_pwm4.ChangeDutyCycle(speed)
                return
            else:
                GPIO.output(40, GPIO.LOW)
                GPIO.output(37, GPIO.HIGH)
                pi_pwm4.ChangeDutyCycle(-speed)
                return
        if forward == 0 and backward == 1:
            if speed >= 0:
                GPIO.output(40, GPIO.LOW)
                GPIO.output(37, GPIO.HIGH)
                pi_pwm4.ChangeDutyCycle(speed)
                return
            else:
                GPIO.output(40, GPIO.HIGH)
                GPIO.output(37, GPIO.LOW)
                pi_pwm4.ChangeDutyCycle(-speed)
                return
        if forward == 0 and backward == 0:
            GPIO.output(40, GPIO.LOW)
            GPIO.output(37, GPIO.LOW)
        if forward == 1 and backward == 1:
            if speed >= 0:
                pi_pwm4.ChangeDutyCycle(speed)
            else:
                pi_pwm4.ChangeDutyCycle(-speed)
    return

def updateEngines(speed):
    if speed >= 0:
        pi_pwm1.ChangeDutyCycle(speed)
        pi_pwm2.ChangeDutyCycle(speed)
        pi_pwm3.ChangeDutyCycle(speed)
        pi_pwm4.ChangeDutyCycle(speed)
        return
    else:
        pi_pwm1.ChangeDutyCycle(-speed)
        pi_pwm2.ChangeDutyCycle(-speed)
        pi_pwm3.ChangeDutyCycle(-speed)
        pi_pwm4.ChangeDutyCycle(-speed)
        return    
# variables

threshold = 0.30
delayAxis = 0.05
delayButton = 0.05
speed = 40
speed1 = 0
speed2 = 0
speed3 = 0
speed4 = 0

controlMode = 1

while not giveup:

    # Check for any queued events and then process each one
    events = pygame.event.get()
    for event in events:
        print ('%s' % event)
        print ('%s' % event.type)
                    
    # Check if one of the joysticks has moved  L jest po skosie !
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0: # L prawo lewo
                if abs(event.value) > threshold and event.value > 0:
                    if speed2 < 100:
                        speed2 += 10
                if abs(event.value) > threshold and event.value < 0:
                    if speed2 > -100:
                        speed2 -= 10
                updateEngine(2,1,1,speed + speed2)
            if event.axis == 1: # L gora dol
                if abs(event.value) > threshold and event.value > 0:
                    if speed1 < 100:
                        speed1 += 10
                if abs(event.value) > threshold and event.value < 0:
                    if speed1 > -100:
                        speed1 -= 10
                updateEngine(1,1,1,speed + speed1)
#             if event.axis == 2: # L3 odchylenie
#                 sleep(delayAxis)
            if event.axis == 3: # R prawo lewo
                if abs(event.value) > threshold and event.value > 0:
                    if speed3 < 100:
                        speed3 += 10
                if abs(event.value) > threshold and event.value < 0:
                    if speed3 > -100:
                        speed3 -= 10
                updateEngine(3,1,1,speed + speed3)
            if event.axis == 4: # R gora dol
                if abs(event.value) > threshold and event.value > 0:
                    if speed4 < 100:
                        speed4 += 10
                if abs(event.value) > threshold and event.value < 0:
                    if speed4 > -100:
                        speed4 -= 10
                updateEngine(4,1,1,speed + speed4)
#             if event.axis == 5: # R3 odchylenie
#                 sleep(delayAxis)
            
        # eventy naciskanie przycisku
        if event.type == pygame.JOYBUTTONDOWN: # czy wcisnieto przycisk
            if event.button == 0: # cross
                controlMode = 1
            if event.button == 1: # circle
                speed = 0
                speed1 = 0
                speed2 = 0
                speed3 = 0
                speed4 = 0
                updateEngines(speed)
            if event.button == 2: # triangle
                updateEngines(0)
            if event.button == 3: # square
                updateEngine(1,0,0,speed + speed1)
                updateEngine(2,0,0,speed + speed2)
                updateEngine(3,0,0,speed + speed3)
                updateEngine(4,0,0,speed + speed4)
            if event.button == 4: # L1
                updateEngine(1,0,1,speed + speed1)
                updateEngine(2,0,1,speed + speed2)
                updateEngine(3,1,0,speed + speed3)
                updateEngine(4,1,0,speed + speed4)
            if event.button == 5: # R1
                updateEngine(1,1,0,speed + speed1)
                updateEngine(2,1,0,speed + speed2)
                updateEngine(3,0,1,speed + speed3)
                updateEngine(4,0,1,speed + speed4)
            if event.button == 6: # L2 # L2 i R2 dzialaja tez jako osie
                if speed > 0:
                    speed -= 10
                updateEngines(speed)
            if event.button == 7: # R2
                if speed < 100:
                    speed += 10
                updateEngines(speed)
            if event.button == 8: # select
                speed1 = 0
                speed2 = 0
                speed3 = 0
                speed4 = 0
            if event.button == 9: # start
                speed = 40
#             if event.button == 10: # ps button
#             if event.button == 11: # L3 # L3 = wcisniecie prawej galki joysticka
#             if event.button == 12: # R3
            if event.button == 13: # /\
                updateEngine(1,1,0,speed + speed1)
                updateEngine(2,1,0,speed + speed2)
                updateEngine(3,1,0,speed + speed3)
                updateEngine(4,1,0,speed + speed4)
            if event.button == 14: # \/
                updateEngine(1,0,1,speed + speed1)
                updateEngine(2,0,1,speed + speed2)
                updateEngine(3,0,1,speed + speed3)
                updateEngine(4,0,1,speed + speed4)
            if event.button == 15: # <
                updateEngine(1,0,1,speed + speed1)
                updateEngine(2,1,0,speed + speed2)
                updateEngine(3,0,1,speed + speed3)
                updateEngine(4,1,0,speed + speed4)
            if event.button == 16: # >
                updateEngine(1,1,0,speed + speed1)
                updateEngine(2,0,1,speed + speed2)
                updateEngine(3,1,0,speed + speed3)
                updateEngine(4,0,1,speed + speed4)

        # eventy puszczanie przycisku
        if event.type == pygame.JOYBUTTONUP: # czy puszczono przycisk
            if event.button == 0: # cross
                sleep(delayButton)
            if event.button == 1: # circle
                updateEngines(speed)
            if event.button == 2: # triangle
                sleep(delayButton)
            if event.button == 3: # square
                sleep(delayButton)
            if event.button == 4: # L1
                sleep(delayButton)
            if event.button == 5: # R1
                sleep(delayButton)
            if event.button == 6: # L2
                sleep(delayButton)
            if event.button == 7: # R2
                sleep(delayButton)
            if event.button == 8: # select
                sleep(delayButton)
            if event.button == 9: # start
                sleep(delayButton)
            # 10 = ps button
            if event.button == 11: # L3
                sleep(delayButton)
            if event.button == 12: # R3
                sleep(delayButton)
            if event.button == 13: # /\
                sleep(delayButton)
            if event.button == 14: # \/
                sleep(delayButton)
            if event.button == 15: # <
                sleep(delayButton)
            if event.button == 16: # >
                sleep(delayButton)

if giveup:
    print("Error: Controller not found")

GPIO.cleanup()
