class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.idx_dic = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx_dic[val].add(len(self.list))
        self.list.append(val)
        return len(self.idx_dic[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx_dic[val]:
            return False
        remove_idx = self.idx_dic[val].pop()
        last_val = self.list[-1]
        self.list[remove_idx] = last_val
        self.idx_dic[last_val].add(remove_idx)
        self.idx_dic[last_val].remove(len(self.list) - 1)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list)