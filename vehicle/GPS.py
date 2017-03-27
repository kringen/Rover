import serial
from pynmea import nmea
import Com

ser = serial.Serial('/dev/ttyAMA0',9600)
gpgga = nmea.GPGGA()

def getCoords():
     coords = {}
     while 1:
          data = ser.readline()
          if (data.startswith('$GPGGA')):
              gpgga.parse(data)
              coords["latitude"] = gpgga.latitude
              coords["longitude"] = gpgga.longitude
              coords["altitude"] = gpgga.antenna_altitude
              coords["altUnits"] = gpgga.altitude_units
              coords["sats"] = gpgga.num_sats
              break
     return coords

if __name__ == '__main__':
     coords = getCoords()
     print(coords)
