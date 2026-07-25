"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            # If already cloned, return it
            if node in oldToNew:
                return oldToNew[node]

            # Create a copy of the node
            copy = Node(node.val)

            # Save in dictionary
            oldToNew[node] = copy

            # Clone all neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)