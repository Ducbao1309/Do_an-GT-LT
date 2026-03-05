class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        children = 0
        cookie_index = 0
        while cookie_index < len(s) and children < len(g):
            if s[cookie_index] >= g[children]:
                children += 1
            cookie_index += 1
        return children