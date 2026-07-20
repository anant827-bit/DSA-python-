# Binary Tree
class node():
    def __init__(self, data):
        self.left=None
        self.data=data
        self.right=None

class binary_tree():
    def __init__(self):
        self.start=None

    def insert_nodes(self, root):
        item=int(input("Enter value to insert:"))

        if item==-1:
            return None
        
        root=node(item)

        print(f"Enter values to insert in left of {item}")
        root.left=self.insert_nodes(root.left)

        print(f"Enter values to insert in right of {item}")
        root.right=self.insert_nodes(root.right)

        return root

    def preorder(self,root):
        if root is None:
            return
        
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

b=binary_tree()
b.start=b.insert_nodes(b.start)

print(b.preorder(b.start))