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

    def find_key(self, key):
        if self.start is None:
            return False
        
        ptr=self.start
        while ptr:

            if ptr.data==key:
                return True
            
            elif ptr.data>key:
                ptr=ptr.left

            else:
                ptr=ptr.right

        return False

    # For Binary Tree
    def key(self, root, item):
        if root is None:
            return False
        
        if root.data==item:
            return True
        
        return self.key(root.left, item) or self.key(root.right, item)

    def search_key(self, root, item):
        if root is None:
            return False
        
        if root.data==item:
            return True
        elif root.data>item:
            return self.search_key(root.left, item)
        else:
            return self.search_key(root.right, item)
        

    
t=BST()
t.insert_nodes(8)
t.insert_nodes(27)
t.insert_nodes(17)
t.insert_nodes(26)
t.insert_nodes(5)
t.insert_nodes(11)

t.display()
print()
print("Does tree contain 17?", t.find_key(17))

print()
print("Does tree contain 17?", t.search_key(t.start, 46))