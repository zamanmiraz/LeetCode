class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        1   0   0   0
        1   0
        """
        def getList(num):
            numList = []
            while num:
                numList.append(num % 10)
                num //= 10
            return numList[::-1]

        def match(numList, trie):
            count = 0
            for num in numList:
                if num in trie:
                    trie = trie[num]
                    count += 1
                else:
                    return count
            return count
        
        trie = {}
        for num in arr1:
            numList = getList(num)
            t = trie
            for n in numList:
                if n not in t:
                    t[n] = {}
                t = t[n]
        res = 0
        for num in arr2:
            res = max(res, match(getList(num), trie))
        return res
