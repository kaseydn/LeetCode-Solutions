class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        #Construct copies of nodes and map them to their originals
        node_cache = { None: None}
        curr = head
        while curr:
            node_cache[curr] = Node(curr.val)
            curr = curr.next
        
        #Iterate through the original list populating randoms and linking the new list
        curr = head
        while curr:
            node_cache[curr].next = node_cache[curr.next]
            node_cache[curr].random = node_cache[curr.random]

            curr = curr.next
        return node_cache[head]

        