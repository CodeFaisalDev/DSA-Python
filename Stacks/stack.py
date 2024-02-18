class Stack:
    def __init__(self, max_size = None):
        self.stack = []
        self.max_size = max_size
    
    # Is Empty
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    # Is Full
    def isFull(self):
        if len(self.stack) == self.max_size:
            return True
        else:
            return False

    # Push Into Stack
    def push(self, value):
        if self.isFull():
            print("Stack Overflow Can't Push into the stack")
            return
        else:
            self.stack.append(value)
    
    # Pop from Stack
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        else:
            poped_item = self.top()
            self.stack.pop()
            return poped_item
    
    # Get Top of the Stack
    def top(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        else:
            t = len(self.stack) - 1
            return self.stack[t]
        
    #display Stack
    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i], "->")
        
def main():
    s1 = Stack(max_size=5)

    # print(s1.top())

    s1.push(3)
    s1.push(5)
    s1.push(7)
    s1.push(4)
    s1.push(1)
    s1.push(10)

    # s1.display()

    # print(s1.top())
    # # print(s1.isEmpty())
    # print(s1.isFull())

    s1.pop()
    s1.display()

    print("Poped item:", s1.pop())

    
if __name__ == "__main__":
    main()


    