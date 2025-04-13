from collections import defaultdict
from typing import List


class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def build(self, words: List[str]):
        for word in words:
            it = self.root
            for c in word:
                it = it.children[c]
            it.is_word = True
    
    def get_suggestions(self, word: str):
        matches = []
        it = self.find(word)
        self.match_recursively(it, word, matches)
        return matches
    
    def find(self, word: str) -> TrieNode:
        it = self.root
        for c in word:
            if not c in it.children:
                return []
            it = it.children[c]
        return it
    
    def match_recursively(self, it: TrieNode, match: str, matches: List[str]):
        if len(matches) == 3:
            return
        if it.is_word:
            matches.append(match)

        for child in it.children: 
            self.match_recursively(it.children[child], match + child, matches)
        return

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        trie = Trie()
        trie.build(products)
        ans = []

        prefix = ''
        for c in searchWord:
            prefix += c
            ans.append(trie.find_match(prefix))
        return ans
    