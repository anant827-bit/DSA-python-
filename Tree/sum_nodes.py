# Sum of nodes in tree
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

    def sum_nodes(self, root):
        sum=0
        if root is None:
            return sum
        
        sum+=root.data

        if root.left:
            sum=sum + self.sum_nodes(root.left)
        if root.right:
            sum=sum + self.sum_nodes(root.right)

        return sum
    
t=tree()
t.start=t.levelwise_insert(t.start)

t.display()
print()
print("Sum of nodes:", t.sum_nodes(t.start))