# Sum of nodes at kth level in a tree
class node:
    def __init__(self, data):
        self.left=None
        self.data=data
        self.right=None

class tree:
    def __init__(self):
        self.start=None

    def insert(self, root):
        if root is None:
            value_root=int(input("Enter root value:"))
            root=node(value_root)

        queue=[root]

        while queue:
            value=queue.pop(0)

            left=int(input(f"Enter value to be inserted in left of {value.data}:"))
            if left!=-1:
                value.left=node(left)
                queue.append(value.left)

            right=int(input(f"Enter value to be inserted in the right of {value.data}:"))
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

            print(value.data, end="  ")
            if value.left:
                queue.append(value.left)

            if value.right:
                queue.append(value.right)

    def sum_k(self, k):
        sum=0
        if self.start is None:
            return sum
        
        level=1
        queue=[self.start,None]

        while queue and level<k:
            value=queue.pop(0)

            if value is None:
                if queue:
                    queue.append(None)
                level+=1
                continue

            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)

        while queue:
            val=queue.pop(0)
            if val is not None:
                sum = sum + val.data

        return sum
        

t=tree()
t.start=t.insert(t.start)
t.display()

print()

print("Sum of nodes at level 3:", t.sum_k(1))