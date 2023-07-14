#This script is inspired by the instructions I was able to find from the following website:
#https://www.ics.com/blog/control-raspberry-pi-gpio-pins-python

import RPi.GPIO as GPIO
import time
import asyncio
from kasa import SmartPlug, Discover
import subprocess

switch = 36

found_devices = asyncio.run(Discover.discover())
strDevices = str(found_devices)
strDevices = strDevices.split(',')
famSwitch = next(item for item in strDevices if 'Family Room' in item)
famSwitch = famSwitch.split(':')[0]
famIP = famSwitch.split(':')[0].replace("'",'').replace(' ','').replace('{','')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.IN)

def smrtPlug():
    p = SmartPlug(famIP)
    print('getting switch status update')
    stat = subprocess.run(['kasa', '--host', famIP, 'sysinfo'], capture_output=True, text=True).stdout
    #time.sleep(1)
    print(stat)
    if int(stat.split(',')[20].split(':')[1]) == 1:
        subprocess.run(['kasa', '--type', 'plug', '--host', famIP, 'off'])
        #await p.turn_off()
    else:
        subprocess.run(['kasa', '--type', 'plug', '--host', famIP, 'on'])
        #await p.turn_on()

#    while True:
#        try:
#            await p.update()  # Request the update
#            break
#        except:
#            pass
#    print('done getting status')
#    if p.sys_info['relay_state'] == 1:
#        await p.turn_off()  # Turn the device off
#        await asyncio.sleep(1)
#    else:
#        await p.turn_on()  # Turn the device off
#        await asyncio.sleep(1)
#    #await p.close()


def smrtSwitch():
    p = SmartPlug(famIP)
    p.update()
    print(p.sys_info['relay_state'])

while True:
    if GPIO.input(switch) == 1:
        smrtPlug()
        #smrtPlug()
        while GPIO.input(switch) == 1:
            pass
        time.sleep(0.5)
        #asyncio.close()
