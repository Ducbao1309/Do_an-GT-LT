class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        digits = ""
        for c in number:
            if c.isdigit():
                digits += c
        result = []
        i = 0
        n = len(digits)
        while n - i > 4:
            result.append(digits[i:i+3])
            i += 3
        if n - i == 4:
            result.append(digits[i:i+2])
            result.append(digits[i+2:i+4])
        else:
            result.append(digits[i:])
        return "-".join(result)