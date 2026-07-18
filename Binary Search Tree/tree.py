# Inorder traversal in binary search tree gives a sorted sequence
class Node():
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

class tree():
    def __init__(self):
        self.start=None

    def add(self, item):
        new_node=Node(item)

        if self.start==None:
            self.start=new_node
            return

        else:
            ptr=self.start
            while True:
                if item<ptr.data:

                    if ptr.left==None:
                        ptr.left=new_node
                        return
                    ptr=ptr.left

                elif item>ptr.data:

                    if ptr.right==None:
                        ptr.right=new_node
                        return
                    ptr=ptr.right

                else:
                    print("Error: Duplicate Value.")
                    return

    def preorder(self, root):
        if root==None:
            return
        
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    

    def inorder(self, root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    def bfs(self):
        if self.start==None:
            return
        
        queue=[self.start]

        while queue:
            node=queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

t=tree()
t.add(8)
t.add(5)
t.add(17)
t.add(26)


t.preorder(t.start)
print()
t.inorder(t.start)
print()
t.postorder(t.start)
print()
t.bfs()