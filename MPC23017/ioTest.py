import smbus
import time

# For the Raspberry PI this is the I2C buss address
bus = smbus.SMBus(1)

# Address of the chip next to the input voltage
MPC23017_0 = 0x21

# MPC23017_1 = ???

# Microchip MCP23017 Registers
#   Main registers we need to access for GPIO operation
IODIRA = 0x00
IODIRB = 0x01
OLATA  = 0x14
OLATB  = 0x15

# Direction IODIRx registers
#   0 = Output   1 = Input



# Set port registers to output
bus.write_byte_data(MPC23017_0, IODIRA, 0x00)
bus.write_byte_data(MPC23017_0, IODIRB, 0x00)
# bus.write_byte_data(MPC23017_1, IODIRA, 0x00)
# bus.write_byte_data(MPC23017_1, IODIRB, 0x00)


# Blink x times
print "Blinking"
delay = 0.04
for x in range(0, 20):
    # Turn off all port-A bits
    bus.write_byte_data(MPC23017_0, OLATA, 0x00)
    time.sleep(delay)
    # Set LSB of port-A high
    bus.write_byte_data(MPC23017_0, OLATA, 0x01)
    time.sleep(delay)

print "    Done blinking"
