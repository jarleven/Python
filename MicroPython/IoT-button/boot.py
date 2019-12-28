# This file is executed on every boot (including wake-boot from deepsleep)
import myConfig
import network
import time
from machine import WDT


wdt = WDT()  # enable watchdog timer
print("")
print("Booting...")

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)


def do_connect():

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(myConfig.AP, myConfig.KEY)
        while not sta_if.isconnected():
            wdt.feed()
            pass
    print('network config:', sta_if.ifconfig())


print('disable AP')
ap_if.active(False)


wdt.feed()
do_connect()
wdt.feed()

