class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    
def inorderTriversal(root):
    if root:
        inorderTriversal(root.left)
        print(root.data, end=" ")
        inorderTriversal(root.right)

def preorderTriversal(root):
    if root:
        print(root.data, end=" ")
        preorderTriversal(root.left)
        preorderTriversal(root.right)

def postorderTriversal(root):
    if root:
        postorderTriversal(root.left)
        postorderTriversal(root.right)
        print(root.data, end=" ")
        


def main():
    root = Node(12)
    # root.printTree()

    root.insert(6)
    root.insert(14)
    root.insert(3)

    # root.printTree()
    inorderTriversal(root)
    print("\n")
    preorderTriversal(root)
    print("\n")
    postorderTriversal(root)


if __name__ == "__main__" :
    main() 