# Root to leaf paths
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
                print("Error: Duplicate values.")
                return
            
    def display(self):
        if self.start is None:
            return
        
        queue=[self.start, None]

        while queue:
            value=queue.pop(0)

            if value is None:
                print()
                if queue:
                    queue.append(None)
                continue

            print(value.data, end="  ")
            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)

    def root_to_leaf(self, root, queue):
        if root is None:
            return
        
        queue.append(root.data)

        if root.left is None and root.right is None:
            self.printPath(queue)
        else:
            self.root_to_leaf(root.left, queue)
            self.root_to_leaf(root.right, queue)

        queue.pop()        

    def printPath(self, queue):
        for i in range(len(queue)):
            print(queue[i], end=" ")
        print()

t=BST()
t.insert_nodes(8)
t.insert_nodes(5)
t.insert_nodes(17)
t.insert_nodes(27)
t.insert_nodes(11)

t.display()
print()

print("Root to leaf paths:")
queue=[]
t.root_to_leaf(t.start, queue)