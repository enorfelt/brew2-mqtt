import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode


class PressureSensor:

    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.ads.gain = 1
        self.ads.mode = Mode.CONTINUOUS
        self.chan = AnalogIn(self.ads, ADS.P0)

    def read(self):
        value = self.chan.value
        volt = self.chan.voltage
        return {"value": value, "voltage": volt} 
