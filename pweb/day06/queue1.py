from multiprocessing import Queue

#创建队列
q = Queue(3)
q.put(1)
print(q.full())
q.put(2)
q.put(3)
# q.put(4,block = False)
print(q.qsize(),'条')
print(q.full())
# q.put(4)
print(q.get())
print(q.qsize(),'条')
print(q.get())
print(q.qsize(),'条')
print(q.get())
print(q.qsize(),'条')
print(q.empty())