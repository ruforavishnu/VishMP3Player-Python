import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
	time.sleep(.5)#pretend to do some work
	with print_lock:
		print(threading.current_thread().name, worker)

def threader():
	while True:
		worker = q.get() #gets a worker from the queue

		exampleJob(worker) # Run the example job with the avail worker in queue(thread)

		q.task_done() #completed the job


q = Queue() # Create the queue

#How many threads are we going to allow for
for x in range(10):
	t = threading.Thread(target=threader)

	t.daemon = True # classifying as a daemon, so they will die when the main dies
	t.start() #begins, must come after daemon definition

start = time.time()

for worker in range(20): #20 jobs assigned
	q.put(worker)

q.join() # wait until Thread terminates

totalTime = time.time() - start
totalTimeStr = str(totalTime)
print("Entire job took:"+ totalTimeStr )

