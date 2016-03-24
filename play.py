
"""
Playing violin code.
LED port 1 = yellow
LED port 2 = red
LED port 3 = green
LED port 4 = orange
triLED port 1 = light for bow
triLED port 2 = light for pitch
Sensor port 1 = knob for bow
Sensor port 3 = distance for pitch
Sensor port 4 = light for hand
Motor port 1 = motor for bow
Servo port 1 = A string
Servo port 2 = D string
Servo port 3 = violin movement
"""

from hummingbird import Hummingbird
from time import sleep
import servos

def isHandled(humm) :
    handHeld = 0
    handLight = humm.get_light_sensor(4)
    if handLight < 10 :
        handHeld = 1
    return handHeld

def singleLedsOn(humm) :
    humm.set_single_led(1,255)
    humm.set_single_led(2,255)
    humm.set_single_led(3,255)
    humm.set_single_led(4,255)

def triLedsOff(humm) :
    humm.set_tricolor_led(1,0,0,0)
    humm.set_tricolor_led(2,0,0,0)

def singleLedsOff(humm) :
    humm.set_single_led(1,0)
    humm.set_single_led(2,0)
    humm.set_single_led(3,0)
    humm.set_single_led(4,0)

print("Playing...")
humm = Hummingbird()
motorDir = 1
noteLength = .1

while 1:

    #when not handheld, leds blink
    if not isHandled(humm) :
        singleLedsOn(humm)
        triLedsOff(humm)
        servos.playA(humm)
        servos.playLowD(humm)
        humm.set_motor(1,0)

    for i in range(0,4):
        if not isHandled(humm) :
            sleep(.1)

    singleLedsOff(humm)

    for i in range(0,4):
        if not isHandled(humm) :
            sleep(.1)
    
    #when handheld, pitch and speed controled by user
    if isHandled(humm) :
        knobValue = 255 - humm.get_knob_value(1)
        if knobValue < 240 :
            noteLength = .1
            humm.set_motor(1, (knobValue+60)/300 )
        else :
             humm.set_motor(1, motorDir*.5)
             noteLength = .2
             motorDir = -motorDir
            
        humm.set_tricolor_led(1,knobValue,knobValue,knobValue)

        distValue = humm.get_distance(3)
        
        if distValue < 10 :
            servos.playLowD(humm)
            humm.set_tricolor_led(2,255,0,0)#red
        elif distValue < 14 :
            servos.playE(humm)
            humm.set_tricolor_led(2,255,125,0)#orange
        elif distValue < 20 :
            servos.playG(humm)
            humm.set_tricolor_led(2,255,255,0)#yellow
        elif distValue < 21 :
            servos.playAandG(humm)
            humm.set_tricolor_led(2,255,255,0)#yellow
        elif distValue < 25 :
            servos.playA(humm)
            humm.set_tricolor_led(2,0,255,0)#green
        elif distValue < 29 :
            servos.playB(humm)
            humm.set_tricolor_led(2,0,0,255)#blue
        elif distValue < 33 :
            servos.playHighD(humm)
            humm.set_tricolor_led(2,125,0,255)#violet
        else : 
            humm.set_tricolor_led(2,0,0,0)
        sleep(noteLength)

humm.close()
