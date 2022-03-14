class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result_value = 0
        map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        max_value=1
        for i in xrange(len(s)-1,-1,-1):
            if map[s[i]]>=max_value:
                max_value = map[s[i]]
                result_value +=map[s[i]]
            else:
                result_value -=map[s[i]]
                
        return result_value