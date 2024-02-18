class Queue:
    def __init__(self, max_size = None):
        self.queue = []
        self.max_size = max_size

    # Is Empty
        
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    # Is Full
    def isFull(self):
        if self.max_size is not None and len(self.queue) == self.max_size:
            return True
        else:
            return False
    
    # Enqueue
    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full Can't enqueue")
            return
        else:
            print(value, "is Enqueued")
            self.queue.append(value)

    # Dequeue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty Can't dequeue")
            return
        else:
            poped = self.queue.pop(0)
            print(poped, " is Dequeued")            
    # Front
    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            print("Queue is empty. No front element.")

    def display(self):
        print("Queue:", self.queue)


def main():
    q1 = Queue(max_size=5)

    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)

    q1.display()  # Output: Queue: [1, 2, 3]

    front_element = q1.front()
    print("Front Element:", front_element)  # Output: Front Element: 1

    q1.dequeue()
     # Output: Dequeued Element: 1

    q1.display()  # Output: Queue: [2, 3]

    q1.dequeue()
    q1.display()

if __name__ == "__main__":
    main()