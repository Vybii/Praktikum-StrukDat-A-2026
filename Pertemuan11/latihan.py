class Node:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None

class BinarySearchTree:
    def __init__(self):
        self.root= None

    def insert(self,data):
        #langkah 1
        new = Node(data)

        #langkah 2
        if self.root is None :
            self.root = new
            return
        
        #langkah 3
        p = self.root
        q = self.root


        #langkah 4
        while q is not None and new.data != p.data :

        #langkah 5
            p = q

        #langkah 6
            if new.data < p.data:
                q = p.left
            else:
                q = p.right

        #langkah 7
        if new.data == p.data:
            print('datanya duplikat')
            return
        
        #langkah 8
        if new.data < p.data:
            p.left= new
        else:
            p.right= new




bst = BinarySearchTree()

bst.insert(77)
bst.insert(66)
bst.insert(11)
bst.insert(33)
bst.insert(55)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end="->")
        in_order(node.right)

in_order(bst.root)

#LATIHAN
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node


def postOrder(node):
    if node is not None :
        postOrder(node.left)
        postOrder(node.right)
        print(node.data, end="->")

def preOrder(node):
    if node is not None:
        print(node.data, end="->")
        preOrder(node.left)
        preOrder(node.right)
        
        


tree = BinaryTree()

tree.insert_root('F')


#Left
tree.insert_left(tree.root, 'B')
tree.insert_left(tree.root.left, 'A')
tree.insert_right(tree.root.left, 'D')
tree.insert_left(tree.root.left.right, 'C')
tree.insert_right(tree.root.left.right, 'E')

#Right
tree.insert_right(tree.root, 'G')
tree.insert_right(tree.root.right, 'I')
tree.insert_left(tree.root.right.right, 'H')

print("\n")
print("pre order")
preOrder(tree.root)

print("\n")
print("in order")
in_order(tree.root)

print("\n")
print("post order")
postOrder(tree.root)