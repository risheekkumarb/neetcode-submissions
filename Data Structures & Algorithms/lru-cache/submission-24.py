class ListNode:
    def __init__(self,key,val,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self): return f'{self.key}-{self.val} --> {self.next}'

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {} # k,node pairs live
        self.left = ListNode(0,0)
        self.right= ListNode(0,0, left=self.left)
        self.left.right = self.right # starter

    def add(self,key,val):
        node = ListNode(key,val)
        self.store[key] = node
        right, left = self.right, self.right.left
        right.left, left.right = node, node
        node.left, node.right  = left, right

    def delete(self,node):
        left,right = node.left, node.right
        left.right, right.left = right, left
        del self.store[node.key]

    def get(self, key: int) -> int:
        # see if its in store
        # if present, get the val from node
        if key in self.store:
            node = self.store[key]
            self.delete(node)
            self.add(node.key,node.val)
            return self.store[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # check if its already there
        # if there delete it and add a new node
        # check for capacity and delete lru
        if key in self.store: self.delete(self.store[key])
        self.add(key,value)

        if len(self.store) > self.cap:
            lru_node = self.left.right
            self.delete(lru_node)

