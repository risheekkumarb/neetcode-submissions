class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.neighbors = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for w in word:
            if w not in node.neighbors:
                node.neighbors[w] = TrieNode(w)
            node = node.neighbors.get(w)
        node.is_end = True

    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.neighbors: return False
            node = node.neighbors.get(w)
        return node.is_end

    def startsWith(self, word):
        node = self.root
        for w in word:
            if w not in node.neighbors: return False
            node = node.neighbors.get(w)
        return True