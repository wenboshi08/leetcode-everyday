from sortedcontainers import SortedDict
class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key is KEY, value is score
        self.key_score = {}
        # key is score, value is the set of KEYS
        self.score_keys = SortedDict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.key_score:
            self.key_score[key] = 1
            if 1 not in self.score_keys:
                self.score_keys[1] = set()
            self.score_keys[1].add(key)
        else:
            pre_score = self.key_score[key]
            val = self.score_keys.get(pre_score)
            if len(val) == 1:
                del self.score_keys[pre_score]
            else:
                val.remove(key)
            new_score = pre_score + 1
            self.key_score[key] = new_score
            if new_score not in self.score_keys:
                self.score_keys[new_score] = set()
            self.score_keys[new_score].add(key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key_score:
            return
        pre_score = self.key_score[key]
        val = self.score_keys.get(pre_score)
        if len(val) == 1:
            del self.score_keys[pre_score]
        else:
            val.remove(key)
        new_score = pre_score - 1
        if new_score == 0:
            del self.key_score[key]
        else:
            self.key_score[key] = new_score
            if new_score not in self.score_keys:
                self.score_keys[new_score] = set()
            self.score_keys[new_score].add(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if len(self.key_score) == 0:
            return ""

        key, val = self.score_keys.peekitem()
        return list(val)[0]

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if len(self.key_score) == 0:
            return ""
        key, val = self.score_keys.peekitem(0)
        return list(val)[0]