# Find height of a tree
class node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

class tree:
    def __init__(self):
        self.start=None

    def levelwise_insert(self, root):
        if root is None:
            value=int(input("Enter root value:"))
            root=node(value)

        queue=[root]

        while queue:
            value=queue.pop(0)

            left=int(input(f"Enter value to be inserted in left of {value.data}:"))
            if left!=-1:
                value.left=node(left)
                queue.append(value.left)

            right=int(input(f"Enter value to be inserted in right of {value.data}:"))
            if right!=-1:
                value.right=node(right)
                queue.append(value.right)

        return root
    
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

            print(value.data, end=" ")
            if value.left:
                queue.append(value.left)

            if value.right:
                queue.append(value.right)

    def height(self,root):
        h=0
        if root is None:
            return h
        
        h = max(self.height(root.left), self.height(root.right)) +1
        
        return h
    
t=tree()
t.start=t.levelwise_insert(t.start)

t.display()
print()
print("Height of tree:", t.height(t.start))