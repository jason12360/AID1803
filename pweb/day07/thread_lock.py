import threading 

a = b = 0

lock = threading.Lock()

def value():
	while True:
		with lock:
			if a != b:
				print("a = %d,b = %d"%(a,b))

t = threading.Thread(target = value)
t.start()

while True:
	with lock:
		a += 1
		b += 1

t.join()