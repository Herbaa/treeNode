class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.tree = None
        
    
    def insert(self, key1, value1):
        def insertt(node, key, value):
            if node == None:
                return TreeNode(key, value)
            
            if key < node.key:
                node.left = insertt(node.left, key, value)
            if key > node.key:
                node.right = insertt(node.right, key, value)
            
            else:
                node.value = value
            return node
        
        self.tree = insertt(self.tree, key1, value1)



    def search(self, key):
        node = self.tree
        
        while node:
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None
    
    def delete(self, key):
        
        def min_node(node):
            while node.left:
                node = node.left
            return node
        
        def deletee(node, key):
            
            if not node:
                return None
            
            if key < node.key:
                node.left = deletee(node.left, key)
            if key > node.key:
                node.right = deletee(node.right, key)
            
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                min = min_node(node.right)
                node.key, node.value = min.key, min.value
                
                node.right = deletee(node.right, min.key)
                
            return node
        
        self.tree = deletee(self.tree, key)
        
        
    def height(self):
        def heightt(node):
            if not node:
                return 0
            
            return 1 + max(heightt(node.left), heightt(node.right))
        return heightt(self.tree)
    
    
    def is_balanced(self):
        def _check(node):
            if not node:
                return 0, True

            left_height, left_balanced = _check(node.left)
            right_height, right_balanced = _check(node.right)

            balanced = (left_balanced and right_balanced and abs(left_height - right_height) <= 1 )

            return 1 + max(left_height, right_height), balanced

        return _check(self.tree)[1]
    
    
    
    
    
    

#использование

tree = BinarySearchTree()

tree.insert(5, 'five')
tree.insert(1, 'one')
tree.insert(10, 'ten')
tree.insert(6, 'six')

print('search 6:', tree.search(6))

print('height:', tree.height())

print('balanced:', tree.is_balanced())

tree.delete(5)

print('delete 3:', tree.search(3))