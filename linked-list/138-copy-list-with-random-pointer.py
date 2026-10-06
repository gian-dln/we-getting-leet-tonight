# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {None : None}
        curr = head 

        while curr:
            node = Node(curr.val)
            copy[curr] = node
            curr = curr.next

        curr = head #curr goes back to head of original list, not copy
        while curr:
            node = copy[curr]  #finds the original node in the copied list
            node.next = copy[curr.next] #assigns the copied node next pointer to the original nodes next pointer
            node.random = copy[curr.random]
            curr = curr.next

        return copy[head]
