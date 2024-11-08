class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_dict={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans=0
        for i in range(len(s)):
            if i<len(s)-1 and r_dict[s[i]]<r_dict[s[i+1]]:
                ans-=r_dict[s[i]]
            else:
                ans+=r_dict[s[i]]
        return ans