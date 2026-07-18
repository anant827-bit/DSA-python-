# Print numbers from X to Y in a tree
class node:
    def __init__(self, data):
        self.left=None
        self.data=data
        self.right=None

class BST:
    def __init__(self):
        self.start=None

    def insert_nodes(self, item):
        new_node=node(item)

        if self.start is None:
            self.start=new_node
            return
        
        ptr=self.start
        while True:
            if item<ptr.data:
                if ptr.left is None:
                    ptr.left=new_node
                    return
                ptr=ptr.left

            elif item>ptr.data:
                if ptr.right is None:
                    ptr.right=new_node
                    return
                ptr=ptr.right

            else:
                print("Eroor: Duplicate values.")
                return
            
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)


    def print_In_range(self, root, x, y):
        if root is None:
            return
        if root.data>=x and root.data<=y:
            self.print_In_range(root.left, x, y)
            print(root.data, end=" ")
            self.print_In_range(root.right, x, y)

        elif root.data>y:
            self.print_In_range(root.left, x, y)

        else:
            self.print_In_range(root.right, x, y)


t=BST()
t.insert_nodes(8)
t.insert_nodes(27)
t.insert_nodes(17)
t.insert_nodes(11)
t.insert_nodes(5)
t.insert_nodes(26)

t.inorder(t.start)
print()

t.print_In_range(t.start, 8, 17)