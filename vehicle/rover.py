import Com
import GPS
import json


def getVehicleDetails(filename):
	with open(filename,'r') as f:
		vehicleDetails = json.load(f)
	return vehicleDetails


if __name__ == "__main__":
	# Get Vehicle ID
	vehicleDetails = getVehicleDetails("vehicleDetails.json")
	vehicleID = vehicleDetails["vehicleID"]

	# Get Vehicle status
	status = GPS.getCoords()
	status["vehicleID"] = vehicleID	
	
	# Send status
	Com.sendData("http://10.0.0.30:5000",status)
	

	print(status)

