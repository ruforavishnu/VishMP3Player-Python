import time,threading


def updateEvery3Seconds():
	print("updating every 3 seconds")


myTimer = threading.Timer(3, updateEvery3Seconds)
myTimer.start()


while True:
		print("inside while true")