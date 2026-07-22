class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()

            current = current.children[ch]

        current.isWord = True

    def search(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return current.isWord

    def startsWith(self, prefix):
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)