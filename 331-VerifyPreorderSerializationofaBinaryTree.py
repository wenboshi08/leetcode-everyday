class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        nodes = preorder.split(',')
        slot = 1
        # initially we have one empty slot to put the root in
        for node in nodes:
            # no empty slot to put the current node
            if slot == 0:
                return False
            # a null node occupy one slot
            if node == "#":
                slot -= 1
            # non-null node will create two slots, but occupy one, net increase 1
            else:
                slot += 1
        return slot == 0