from flask import Flask, Response, request, json, render_template
from kafka import KafkaProducer
import uuid
import datetime


app = Flask(__name__)

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Default end point displays helpful information about the API
@app.route('/', methods = ['GET'])
def api_root():
	data = {
		"sats": "09", 
		"vehicleID": "a29ca5d2-5fbc-4556-a555-469692d52fb1", 
		"altitude": "293.9", 
		"longitude": "08404.47007", 
		"latitude": "3551.90440", 
		"altUnits": "M"  
	}
	
	try:
		print(request.headers)
		return render_template("index.html", data = data )
	except Exception, e:
		return str(e)

#  End point for posting vehicle status.
@app.route('/VehicleStatus',  methods = ['POST'])
def post_readings():
	if request.headers['Content-Type'] == 'application/json':
		
		# Create readingTime
		statusTime = datetime.datetime.now().isoformat()
		
		# Create readingID
		statusID = str(uuid.uuid4())
		
		# Add these to json object
		request.json['statusTime'] = statusTime
		request.json['statusID'] = statusID
		
		# Send to Kafka producer
		producer.send('RoverVehicleStatus', json.dumps(request.json))
		return "JSON Message: " + json.dumps(request.json)
	else:
		return "415 Unsupported Media Type"


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=1)
