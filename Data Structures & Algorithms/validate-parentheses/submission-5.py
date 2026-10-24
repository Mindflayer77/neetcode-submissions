class Solution:
    def isValid(self, string: str) -> bool:
        valid_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        if string[0] not in valid_pairs:
            return False
        stack = [string[0]]
        for c in string[1:]:
            if c in valid_pairs:
                stack.append(c)
            elif stack and valid_pairs[stack[-1]] == c:
                stack.pop(-1)
            else:
                return False
        return True if not stack else False