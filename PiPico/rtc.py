import machine
import utime

rtc = machine.RTC()
rtc.datetime((2020, 1, 21, 2, 10, 32, 36, 0))

while True:
    print(rtc.datetime())
    utime.sleep(1)
