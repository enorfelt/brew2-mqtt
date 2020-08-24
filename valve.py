import board
import busio
import adafruit_mcp4725


class Valve:

    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.dac = adafruit_mcp4725.MCP4725(self.i2c)
        self.dac.value = 0

    def set_value(self, value):
        self.dac.value = value
