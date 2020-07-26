import board
import busio
import adafruit_mcp4725


class Valve:
    i2c = busio.I2C(board.SCL, board.SDA)
    dac = adafruit_mcp4725.MCP4725(i2c)

    def __init__(self):        
        print("init normalized value to {}".format(0))      
        Valve.dac.value = 0

    def setPercentageOpen(self, normalized):
        value = int(normalized)
        print("set normalized value to {}".format(value))
        Valve.dac.value = value
