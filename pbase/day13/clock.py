import time
while True:
    time.sleep(1)
    time_tuple = time.localtime()
    print('%02d:%02d:%02d\r'%time_tuple[3:6],end= '')