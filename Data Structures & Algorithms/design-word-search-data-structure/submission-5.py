class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            if not node: return False
            if i == len(word): return node.is_end
            if word[i] != '.' and word[i] not in node.children: return False

            if word[i] == '.': return any(dfs(i+1,c) for c in node.children.values())
            else: return dfs(i+1, node.children[word[i]])
        
        return dfs(0, self.root)
