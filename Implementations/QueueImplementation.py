from queue import Queue

# initialization
q = Queue()

# to initialize a queue with a particular size :
q = Queue(maxsize = 3)

# to check if the queue is empty or not
# return true or false
q.empty()

#Return True if there are maxsize items in the queue. 
# If the queue was initialized with maxsize=0 (the default), then full() never returns True.
q.full()

# to get to know the size of queue
q.qzise()

# to remove an item from queue
q.get()

# return an item if one is available or else raises queueEmpty
q.get_nowait()

# to insert an item into the queue
q.put(i)

# if queue is full(only when a maxsize is declared) raises queueFull
q.put_nowait(i)
