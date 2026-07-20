# Level-wise Insertion

class node:
    def __init__(self, data):
        self.left=None
        self.data=data
        self.right=None

class level_order:
    def __init__(self):
        self.start=None

    def insert_node(self, root):
        if root is None:
            root_value=int(input("Enter root value:"))
            root=node(root_value)

        queue=[]
        queue.append(root)

        while len(queue)!=0:
            value=queue.pop(0)

            left=int(input(f"Enter value to be inserted in the left of {value.data}:"))
            if left!=-1:
                value.left=node(left)
                queue.append(value.left)

            right=int(input(f"Enter value to be inserted in the right of {value.data}:"))
            if right!=-1:
                value.right=node(right)
                queue.append(value.right)

        return root

    def preorder(self,root):
        if root is None:
            return
        
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def levelwise_show(self):
        if self.start is None:
            return
        
        queue=[self.start,None]
        
        while queue:
            value=queue.pop(0)

            if value==None:
                print()
                if queue:
                    queue.append(None)
                continue

            print(value.data, end=" ")
            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)

b=level_order()
b.start=b.insert_node(b.start)

b.preorder(b.start)
print()
b.levelwise_show()