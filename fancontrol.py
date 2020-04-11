#!/usr/bin/env python3

import subprocess
import time
import datetime
import logging

ON_THRESHOLD  = 47.0  # On threshold in degrees Celsius
OFF_THRESHOLD = 46.9  # Off threshold in degrees Celcius
INTERVAL      = 10    # Interval between temperature measurement in seconds
CTRL_PIN      = 17    # GPIO pin to control the fan

logging.basicConfig(level=logging.NOTSET)
log = logging.getLogger('FanControl')
log.info('started')

def getTemperature():
 output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
 temp_str = output.stdout.decode()

 try:
  return float(temp_str.split('=')[1].split('\'')[0])
 except (IndexError, ValueError):
  log.error("Could not parse temperature output")
  raise RuntimeError('Could not parse temperature output.')

while True:
 temperature = getTemperature()
 print('Temperature: ' + str(temperature))
 # TODO: Read out value on fan status pin, to make sure the fan is not already on.
 if temperature > ON_THRESHOLD:
  log.info('Fan turned on, temperature:' + str(temperature))
  # TODO: Set pin to high
 elif temperature < OFF_THRESHOLD:
  log.info('Fan turned off, temperature: ' + str(temperature))
  # TODO: Set pin to low
 time.sleep(INTERVAL)

log.info('finished')
