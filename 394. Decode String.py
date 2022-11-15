class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        KST:
        Looks like a classis stack problem.
        Add to stack and see magic
        """
        stack = []
        num = 0
        cur_str = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
                continue
            if char == "[":
                stack.append((cur_str, num))
                cur_str = ""
                num = 0
                continue

            if char == "]":
                saved_str, n = stack.pop()
                cur_str = saved_str + (cur_str * n)
                num = 0
                continue

            cur_str += char
            
        return cur_str
