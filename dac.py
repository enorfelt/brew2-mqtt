import board
import busio
import adafruit_mcp4725

i2c = busio.I2C(board.SCL, board.SDA)
dac = adafruit_mcp4725.MCP4725(i2c)
dac.noramlized_value = 0.0
