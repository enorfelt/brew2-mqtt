import board
import busio
import adafruit_mcp4725


class Valve:
  i2c = busio.I2C(board.SCL, board.SDA)
  dac = adafruit_mcp4725.MCP4725(i2c)

  def __init__(self):
    print("init normalized value to {}".format(0.0))
    Valve.dac.noramlized_value = 0.0

  def setPercentageOpen(self, noramlized: float):
    print("set normalized value to {}".format(noramlized))
    Valve.dac.noramlized_value = noramlized
