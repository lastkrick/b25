import requests
import time
import socket
import os

URL = 'https://icanhazip.com'
HOSTNAME = socket.gethostname()
NODE_HOSTNAME = os.environ.get("NODE_NAME")

outputHTML = 0
totalTimesToRun = 100
timeBetweenLoop = .25

def GetHTMLResult():
    requestURL = URL + '?hostname=' + HOSTNAME + '&var2=' + NODE_HOSTNAME
    htmlResult = requests.get(requestURL)

    if outputHTML == 1:
        print(htmlResult.text)

if totalTimesToRun == 0:
    while True:
        GetHTMLResult()
        time.sleep(timeBetweenLoop)
else:
    for i in range(totalTimesToRun):
        GetHTMLResult()

        if(i != totalTimesToRun - 1):
            time.sleep(timeBetweenLoop)
