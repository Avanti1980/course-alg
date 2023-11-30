from queue import Queue 

q = Queue(maxsize=0)

#写入队列数据
q.put(0)
q.put(1)
q.put(2)

#输出当前队列所有数据
print(q.queue)
#删除队列数据，并返回该数据
q.get()
#输也所有队列数据
print(q.queue)