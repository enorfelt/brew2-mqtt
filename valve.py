import board
import busio
import adafruit_mcp4725


class Valve:

    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.dac = adafruit_mcp4725.MCP4725(self.i2c)
        print("init normalized value to {}".format(0))
        self.dac.value = 0

    def set_value(self, value):
        print("set normalized value to {}".format(value))
        self.dac.value = value
