import board
import busio
import adafruit_mcp4725


class Valve:
    

    def __init__(self):        
        print("init normalized value to {}".format(0.0))
        i2c = busio.I2C(board.SCL, board.SDA)
        dac = adafruit_mcp4725.MCP4725(i2c)
        Valve.dac.noramlized_value = 0.0

    def setPercentageOpen(self, normalized):
        value = float(normalized)
        print("set normalized value to {}".format(value))
        print("Yes") if value == 0.5 else print("No")
        i2c = busio.I2C(board.SCL, board.SDA)
        dac = adafruit_mcp4725.MCP4725(i2c)
        dac.noramlized_value = value
