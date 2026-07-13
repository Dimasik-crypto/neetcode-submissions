class Solution:
    def encode(self, strs):
        return ''.join(f'{len(s)}#{s}' for s in strs)
    
    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length
        return res
