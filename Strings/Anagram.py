class Solution:
    def areAnagrams(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False

        count = {}
        for ch in s1:
            count[ch] = count.get(ch, 0) + 1
        for ch in s2:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True