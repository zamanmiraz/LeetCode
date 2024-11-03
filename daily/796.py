class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        ex1:
        a   b   c   d   e
        c   d   e   a   b

        ex2:
        a   b   a   c   d   e
        b   a   c   d   e   a
        """
        if len(s) != len(goal): return False
        return self.kmp_search(s + s, goal)
    
    def kmp_search(self, text, pattern):
        lps = self.compute_lps(pattern)
        text_index = 0
        pattern_index = 0
        while text_index < len(text):
            if text[text_index] == pattern[pattern_index]:
                text_index += 1
                pattern_index += 1
                if pattern_index == len(pattern): return True
            elif pattern_index > 0:
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1
        return False
    def compute_lps(self, pattern):
        lps = [0] * (len(pattern))
        length = 0
        index = 1
        while index < len(pattern):
            if pattern[index] == pattern[length]:
                length += 1
                lps[index] = length
                index += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[index] = 0
                index += 1
        return lps
        
