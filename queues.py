class queues:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.insert(0,item)
    def dequeue(self):
        self.queue.pop(len(self.queue)-1)
    def length(self):
        print(len(self.queue))
    def start(self):
        print(self.queue[len(self.queue)-1])
    def last(self):
        print(self.queue[0])
q1=queues()
q1.enqueue(37)
q1.enqueue(50)
q1.enqueue(9)
q1.enqueue(16)
q1.enqueue(62)
q1.length()
q1.dequeue()
q1.length()
q1.start()
q1.last()