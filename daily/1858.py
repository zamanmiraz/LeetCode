class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
                            k
                        /       \
                    #:k             i
                                /
                            #:ki
        """
        trie = {}
        for word in words:
            t = trie
            for alph in word:
                if alph not in t:
                    t[alph] = {}
                t = t[alph]
            t["#"] = word
        res = ""
        for word in words:
            t = trie
            count = 0
            for alph in word:
                t = t[alph]
                if "#" in t:
                    count += 1
            if count != len(word): continue
            if count > len(res):
                res = word
            if count == len(res):
                res = min(res, word)
        return res
