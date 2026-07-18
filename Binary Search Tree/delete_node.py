# Delete a node from binary search tree
# Case 1 -- Deleting leaf node
# Case 2 -- Deleting node with one child
# Case 3 -- Deleting node with two children

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

    def delete_node(self, root, item):
    
        if root.data>item:
            root.left=self.delete_node(root.left, item)

        elif root.data<item:
            root.right=self.delete_node(root.right, item)

        else:
            # Case 1
            if root.left is None and root.right is None:
                return None
            # Case 2
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Case 3
            IS=self.Inorder_Successor(root.right)
            root.data=IS.data
            root.right=self.delete_node(root.right, IS.data)

        return root
    
    def Inorder_Successor(self, root):
        ptr = root
        while ptr.left:
            ptr=ptr.left

        return ptr
        


t=BST()
t.insert_nodes(8)
t.insert_nodes(27)
t.insert_nodes(11)
t.insert_nodes(17)
t.insert_nodes(46)
t.insert_nodes(5)
t.insert_nodes(6)
t.insert_nodes(4)

t.inorder(t.start)

print()
del_item=int(input("Enter node to be deleted:"))
t.delete_node(t.start, del_item)

t.inorder(t.start)