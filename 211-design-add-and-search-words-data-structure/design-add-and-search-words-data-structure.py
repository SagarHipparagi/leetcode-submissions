class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()

            current = current.children[ch]

        current.isWord = True

    def search(self, word):

        def dfs(index, node):

            if index == len(word):
                return node.isWord

            ch = word[index]

            if ch == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            if ch not in node.children:
                return False

            return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)