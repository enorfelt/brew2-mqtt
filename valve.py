import board
import busio
import adafruit_mcp4725


class Valve:

  def __init__(self):
    self.i2c = busio.I2C(board.SCL, board.SDA)
    self.dac = adafruit_mcp4725.MCP4725(i2c)
    print("init normalized value to {}".format(0.0))
    self.dac.noramlized_value = 0.0

  def setPercentageOpen(self):
    #value = float(normalized)
    print("set normalized value to {}".format(0.5))
    #print("Yes") if value == 0.5 else print ("No")
    self.dac.noramlized_value = 0.5
