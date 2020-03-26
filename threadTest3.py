import _thread
import time

def print_time(threadName, delay):
	count = 0
	while count <100:
		time.sleep(delay)
		count += 1
		print("Threadname is :"+threadName+ ", time is:"+time.ctime(time.time()))



try:
	_thread.start_new_thread(print_time, ("Thread1", 1, ))
	_thread.start_new_thread(print_time, ("Thread2", 3, ))



except Exception as e:
	print("Encountered Exception: Unable to start thread")
	print("Exception message:"+e.message)
	print("Exception arguments:"+ e.args)


while 1:
	pass


