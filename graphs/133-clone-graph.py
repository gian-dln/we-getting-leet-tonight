
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = {}
        clone[node] = Node(node.val)
        stack = [node]

        while stack:
            current = stack.pop()
            for neigh in current.neighbors:
                if neigh not in clone:
                    clone[neigh] = Node(neigh.val)
                    stack.append(neigh)

                clone[current].neighbors.append(clone[neigh])
        
        return clone[node]
        