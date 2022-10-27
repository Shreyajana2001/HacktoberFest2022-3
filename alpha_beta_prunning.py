class Node:
    def __init__(self,data,level,alpha,beta,char,left,right):
        self.data = data
        self.level = level
        self.alpha = alpha
        self.beta = beta
        self.char = char
        self.left = left
        self.right = right
    
    def generateTree(self, root):
        node1 = Node(None, 1, -1000, 1000, 'B', None, None)
        node2 = Node(None, 1, -1000, 1000, 'C', None, None)
        node3 = Node(None, 2, -1000, 1000, 'D', None, None)
        node4 = Node(None, 2, -1000, 1000, 'E', None, None)
        node5 = Node(None, 2, -1000, 1000, 'F', None, None)
        node6 = Node(None, 2, -1000, 1000, 'G', None, None)
        node7 = Node(None, 3, -1000, 1000, 'H', None, None)
        node8 = Node(None, 3, -1000, 1000, 'I', None, None)
        node9 = Node(None, 3, -1000, 1000, 'J', None, None)
        node10 = Node(None, 3, -1000, 1000, 'K', None, None)
        node11 = Node(None, 3, -1000, 1000, 'L', None, None)
        node12 = Node(None, 3, -1000, 1000, 'M', None, None)
        node13 = Node(None, 3, -1000, 1000, 'N', None, None)
        node14 = Node(3, 4, -1000, 1000, None, None, None)
        node15 = Node(17, 4, -1000, 1000, None, None, None)
        node16 = Node(2, 4, -1000, 1000, None, None, None)
        node17 = Node(12, 4, -1000, 1000, None, None, None)
        node18 = Node(15, 4, -1000, 1000, None, None, None)
        node19 = Node(25, 4, -1000, 1000, None, None, None)
        node20 = Node(0, 4, -1000, 1000, None, None, None)
        node21 = Node(2, 4, -1000, 1000, None, None, None)
        node22 = Node(5, 4, -1000, 1000, None, None, None)
        node23 = Node(3, 4, -1000, 1000, None, None, None)
        node24 = Node(2, 4, -1000, 1000, None, None, None)
        node25 = Node(14, 4, -1000, 1000, None, None, None)
        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        node2.left= node5
        node2.right = node6
        node3.left = node7
        node3.right = node8
        node4.left = node9
        node4.right = node10
        node5.left = node11
        node5.right = node12
        node6.left = node13
        node7.left = node14
        node7.right = node15
        node8.left = node16
        node8.right = node17
        node9.left  = node18
        node10.left = node19
        node10.right = node20
        node11.left = node21
        node11.right = node22
        node12.left = node23
        node13.left = node24
        node13.right = node25
        
    
    def pruneTree(self, node):
        if node == None or node.char == None:
            return
        self.pruneTree(node.left)
        self.pruneTree(node.right)
        if node.left.data != None and (node.right == None or node.right.data != None):
            
            if node.level % 2 != 0:
                if node.right == None:
                    
                    node.data = node.left.data
                    node.beta = node.left.data
                    node.alpha = node.left.alpha
                else:
                    mn = min(node.left.data, node.right.data)
                    node.data = mn
                    node.beta = mn
                    node.alpha = node.left.alpha
            else:
                if node.right == None:
                    node.data = node.left.data
                    node.alpha = node.left.data
                    node.beta = node.left.beta
                else:
                    mx = manode.left.data, node.right.data)
                    node.data = mx
                    node.alpha = mx
                    node.beta = node.left.beta
                    
        if node.alpha >= node.beta:
            node.right = None
            return
            
        
    def printTree(self, root):
        if root == None:
            return
        print(root.data, root.alpha, root.beta)
        self.printTree(root.left)
        self.printTree(root.right)
        

root = Node(None, 0, -1000, 1000, 'A', None, None)
root.generateTree(root)
root.pruneTree(root)
root.printTree(root)
print("Final value of root node is", root.data)
