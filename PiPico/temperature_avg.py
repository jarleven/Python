# https://hackspace.raspberrypi.com/books/micropython-pico/pdf
# https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf

# Upgraded with a few list modifying features to average the temerature reading
#
#   Insert and pop
#   remove, max and min
#   copy

#   https://stackoverflow.com/questions/10155684/add-entry-to-beginning-of-list-and-remove-the-last-one
#   https://www.geeksforgeeks.org/find-average-list-python/

import machine
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

myList = []



while True:
  reading = sensor_temp.read_u16() * conversion_factor

# The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
# Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
 
  temperature = 27 - (reading - 0.706)/0.001721
   
  myList.insert(0, temperature)
  if len(myList) > 10:
    myList.pop()
    
    listCopy = myList.copy()

    listCopy.remove(max(listCopy))
    listCopy.remove(min(listCopy))
    
    print(listCopy)
    averagetemperature = sum(listCopy) / len(listCopy)
    print(round(averagetemperature,1))

    utime.sleep(2)
    



        

