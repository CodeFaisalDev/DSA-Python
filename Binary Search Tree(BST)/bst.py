class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, data):
        self.root = self.insert(self.root, data)

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        if data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def _search(self, data):
        return self.search(self.root, data)

    def search(self, root, data):
        if root is None or data == root.data:
            return root
        elif data < root.data:
            return self.search(root.left, data)
        elif data > root.data:
            return self.search(root.right, data)
        return None

    def _inorder_traversal(self):
        self.root = self.inorder_traversal(self.root)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

    def _inorder_predecessor(self):
        self.root = self.inorder_predecessor(self.root)

    def inorder_predecessor(self, root):
        if root.left is None:
            return self.max_in_left(root.right)
        current = root.left
        while current.right is not None:
            current = current.right
        return current

    def max_in_left(self, root):
        while root.right is not None:
            root = root.right
        return root

    def _delete(self, data):
        return self.delete(self.root, data)

    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            predecessor = self.inorder_predecessor(root.left)
            root.data = predecessor.data
            root.left = self.delete(root.left, predecessor.data)

        return root

def main():
    bst = BST()

    bst._insert(50)
    bst._insert(40)
    bst._insert(60)
    bst._insert(35)
    bst._insert(70)

    print("In-order traversal before deletion:")
    bst._inorder_traversal()

    deleted_node = bst._delete(60)
    if deleted_node:
        print("\nDeleted node with data:", deleted_node.data)
    else:
        print("\nNode not found for deletion.")

    print("In-order traversal after deletion:")
    bst._inorder_traversal()

    deleted_node = bst._delete(80)
    if deleted_node:
        print("\nDeleted node with data:", deleted_node.data)
    else:
        print("\nNode not found for deletion.")

    print("In-order traversal after deletion:")
    bst._inorder_traversal()

if __name__ == "__main__":
    main()
