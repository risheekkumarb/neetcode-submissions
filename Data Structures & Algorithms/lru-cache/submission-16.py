class Node:
    def __init__(self,key,val,left=None,right=None):
        self.key, self.val, self.left, self.right = key, val, left, right

class LRUCache:
    def __init__(self, capacity: int):
        self.cap   = capacity
        self.state = {}
        self.left  = Node(0,0)
        self.right = Node(0,0,self.left)
        self.left.right = self.right

    def add_node(self,node):
        node.left, node.right = self.right.left, self.right
        self.right.left.right, self.right.left = node, node

    def del_node(self,node):
        node.left.right, node.right.left = node.right, node.left
    
    def get(self, key: int) -> int:
        if key not in self.state: return -1
        node = self.state[key]
        self.del_node(node)
        self.add_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.state: self.del_node(self.state[key])
        self.state[key] = Node(key,value)
        self.add_node(self.state[key])
        
        if len(self.state) > self.cap:
            lru = self.left.right
            self.del_node(lru)
            del self.state[lru.key]