from hummingbird import Hummingbird
from time import sleep

dString = 76
bothStrings = 85
aString = 94

aLow = 100
aOpen = 120
aHigh = 136

dLow = 123
dOpen = 111
dHigh = 97

def playLowD(humm) :
    #print("low D")
    humm.set_servo(1,aOpen)
    humm.set_servo(2,dOpen)
    humm.set_servo(3,dString)

def playE(humm) :
    #print("E")
    humm.set_servo(1,aOpen)
    humm.set_servo(2,dLow)
    humm.set_servo(3,dString)

def playG(humm) :
    #print("G")
    humm.set_servo(1,aOpen)
    humm.set_servo(2,dHigh)
    humm.set_servo(3,dString)

def playAandG(humm) :
    #print("G and A")
    humm.set_servo(1,aOpen)
    humm.set_servo(2,dHigh)
    humm.set_servo(3,bothStrings)

def playA(humm) :
    #print("A")
    humm.set_servo(1,aOpen)
    humm.set_servo(2,dOpen)
    humm.set_servo(3,aString)

def playB(humm) :
    #print("B")
    humm.set_servo(1,aLow)
    humm.set_servo(2,dOpen)
    humm.set_servo(3,aString)

def playHighD(humm) :
    #print("High D")
    humm.set_servo(1,aHigh)
    humm.set_servo(2,dOpen)
    humm.set_servo(3,aString)

def playNotes(humm) :
    for i in range(0,9):
        playLowD(humm)
        #humm.set_motor(1,1)
        sleep(.1)
        playE(humm)
        #humm.set_motor(1,-1)
        sleep(.1)
        playG(humm)
        #humm.set_motor(1,1)
        sleep(.1)
        playA(humm)
        #humm.set_motor(1,-1)
        sleep(.1)
        playB(humm)
        #humm.set_motor(1,1)
        sleep(.1)
        playHighD(humm)
        #humm.set_motor(1,-1)
        sleep(.1)
    
#humm = Hummingbird
#playNotes(humm)
#humm.close()



