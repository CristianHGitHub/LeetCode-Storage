class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for ch_s, ch_t in zip(s, t):
            # Check if we already mapped s → t
            if ch_s in s_to_t:
                if s_to_t[ch_s] != ch_t:
                    return False
            else:
                s_to_t[ch_s] = ch_t

            # Check if we already mapped t → s
            if ch_t in t_to_s:
                if t_to_s[ch_t] != ch_s:
                    return False
            else:
                t_to_s[ch_t] = ch_s

        return True
