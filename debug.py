import time
import json

from pressure_sensor import PressureSensor
# The callback for when the client receives a CONNACK response from the server.

pressureSensor = PressureSensor()


try:
    while True:
        print(json.dumps(pressureSensor.read()))
        time.sleep(1.0)
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass

