class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:

    def __init__(self, levels=30):
        self.heads = [Node(-math.inf) for _ in range(levels)]
        for c, n in zip(self.heads, self.heads[1:]):
            c.down = n
        
    def search(self, target: int) -> bool:
        cur = self.heads[0]
        while cur:
            if cur.next is None or cur.val < target < cur.next.val:
                cur = cur.down
            elif cur.next and target == cur.next.val:
                return True
            else:
                cur = cur.next
        return False
        
    def add(self, num: int) -> None:
        stack = []
        cur = self.heads[0]
        prev = None
        while cur:
            if cur.next is None or cur.val < num <= cur.next.val:
                stack.append(cur)
                cur = cur.down
            else:
                cur = cur.next
        while stack:
            cur = stack.pop()
            node = Node(num)
            node.next, cur.next = cur.next, node
            if prev:
                node.down = prev
            prev = node
            if random.randint(0, len(self.heads)-1) < len(self.heads)-1:
                break

    def erase(self, num: int) -> bool:
        b, cur = False, self.heads[0]
        while cur:
            if cur.next is None or cur.val < num <= cur.next.val:
                if cur.next and cur.next.val == num:
                    b, cur.next = True, cur.next.next
                cur = cur.down
            else:
                cur = cur.next
        return b
