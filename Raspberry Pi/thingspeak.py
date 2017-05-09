import serial
import urllib
import requests
from random import randint

#For sending POST requests
threshold=70

def tweet_message(message):
        payload={
                 'api_key':'H9MA5XO765KWGNYQ',
                 'status':message,
                 'Host':'api.thingspeak.com',                                                    'Content-Type':'application/x-www-form-urlencoded'
                }

        url='https://api.thingspeak.com/apps/thingtweet/1/statuses/update'
        response=requests.post(url,params=payload)
        if response.headers['status']=='200 OK':
                print " Tweet Alert Sent! "
        else:
                print " Tweet Send Failed ",response.headers['status']

url='https://api.thingspeak.com/update'

ser1 = serial.Serial('/dev/ttyACM2',9600)      #FIRST ARDUINO CONNECTION
ser2 = serial.Serial('/dev/ttyACM3',9600)      #SECOND ARDUINO CONNECTION
s = [0,1]
while True:
                read_serial_1=ser1.readline()
        #       read_serial_1=randint(71,71)
        #       read_serial_2=randint(71,71)
                read_serial_2=ser2.readline()
                #print read_serial_1," and ",read_serial_2
                payload={'api_key':'AV76218U0YX1TWNZ',
                  'field1':str(read_serial_1),
                  'field2':str(read_serial_2)
        }
                response=requests.post(url,params=payload)
                if response.headers['status']=='200 OK':
                        print " Arduino 1 value:",read_serial_1,"\n Arduino 2 value",read_serial_2
                        print "\n Data Sent to ThingSpeak "
                        if read_serial_1>threshold or read_serial_2>threshold:
                            tweet_message("GARBAGE BIN values above threshold value of 50cm.\n"+"  Garbage Bin 1 trash level: "+str(read_serial_1)+"\n  Garbage Bin 2 trash level: "+str(read_serial_2)+" \n\n  Schedule Cleaning!  ")
                                #tweet_message("Arduino 1:"+str(read_serial_1)+"Arduino 2:"+str(read_serial_2))
                else:
                        print "Data Send Failed",response.headers['status']


