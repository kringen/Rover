import json
import urllib2

def sendData(url, data):
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))

if __name__ == '__main__':
    data = {
        "name":"value"
        }
    sendData("http://10.0.0.30:5000/StatusUpdate",data)
