#A queue is a useful data structure in programming. 
# It is similar to the ticket queue outside a cinema hall, 
# where the first person entering the queue is the first person who gets the ticket.
#Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self,item):
        if self.queue.length <1:
            return None
        return self.queue.pop(0)
    def display_queue(self):
        print(self.queue)

Queue = Queue()
Queue.enqueue(2)
Queue.display_queue()