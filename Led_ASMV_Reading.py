#! /usr/bin/python

import serial
from time import sleep

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )

keepGoing = False;
go = None;
starter = None;
done = False;
check = None;
getColor = False;

while not done:

    check = raw_input("Done? (y/n) ")

    if (check == "y"):
        done = True;
        break
    else:
        check = None;
        starter = None;
        done = False;

    while starter == None:
        starter = raw_input("getColor (a) or makeBlink (b)? ")

        if (starter == "a"):
            getColor = True;

        if (starter == "b"):
            keepGoing = True;

    while getColor:
        
        starter = None;
        raw_input("Press Enter to get the current color of the Astable Multivibrator")
        bluetoothSerial.write("abcd")
        print bluetoothSerial.readline()

        break
            

    while keepGoing:
        count = None
        starter = None
        while count < 7:
            try:
                count = int(raw_input( "please enter the number of times to blink" ))
  
                bluetoothSerial.write( str(count))
                print bluetoothSerial.readline()
        
                go = raw_input("go or stop?")

                if (go == "stop"):
                    keepGoing = False;
                    break
                if (go == "go"):
                    keepgoing = True;
                else:
                    print "Couldn't discern stop or go, loop ended"
                    keepGoing = False
                    break
            except:
                pass
serial.close();
print "Bye!"
