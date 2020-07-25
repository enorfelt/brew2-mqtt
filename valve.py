import board
import busio
import adafruit_mcp4725

class Valve: 
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.dac = adafruit_mcp4725.MCP4725(self.i2c)
        self.dac.noramlized_value = 0.0

    def setPercentageOpen(self, noramlized: float):
        self.dac.noramlized_value = noramlized