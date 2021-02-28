class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        # construct the Trie
        trie = TrieNode()

        for i, word in enumerate(words):
            word = word[::-1]
            current_level = trie
            for j, c in enumerate(word):
                # check if the remainder of the word is a palindrome
                if word[j:] == word[j:][::-1]:
                    current_level.palindrome_suffixes.append(i)
                # move down the trie
                current_level = current_level.next[c]
            current_level.ending_word = i

        # look up each word in the Trie and find palindrome pairs
        solutions = []
        for i, word in enumerate(words):
            current_level = trie
            for j, c in enumerate(word):
                # check for case 3, i = CATSOLOS to find j = CAT
                if current_level.ending_word != -1:
                    if word[j:] == word[j:][::-1]:
                        solutions.append([i, current_level.ending_word])
                if c not in current_level.next:
                    break
                else:
                    current_level = current_level.next[c]
            # case 1: i = CAT to find j = CAT, i = CAT to find j = CATSOLOS
            # only happend after the entire word is iterated
            else:
                # check for case 1
                if current_level.ending_word != -1 and current_level.ending_word != i:
                    solutions.append([i, current_level.ending_word])
                # check for case 2
                for j in current_level.palindrome_suffixes:
                    solutions.append([i, j])
        return solutions


class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.ending_word = -1
        self.palindrome_suffixes = []