class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False
        s = s.strip()
        num_flag = False
        dot_flag = False
        e_flag = False
        for index, c in enumerate(s):
            if '0' <= c <= '9':
                num_flag = True
            elif c == '.':
                # 前面不能出现 . 或者 e
                if dot_flag or e_flag:
                    return False
                dot_flag = True
            elif c == 'e' or c == 'E':
                # 前面不能出现 e ，必须出现数字
                if e_flag or (not num_flag):
                    return False
                e_flag = True
                num_flag = False
            elif c == '-' or c == '+':
                if index != 0 and s[index - 1] != 'e' and s[index - 1] != 'E':
                    return False
            else:
                return False

        return num_flag


s = Solution()
print(s.isNumber("46.e3"))
