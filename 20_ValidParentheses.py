class Solution:
    def isValid(self, s: str) -> bool:
        save = []
        length = len(s)
        # if length % 2 == 1:
        #     return False
        for i in range(length):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                save.append(s[i])
            else:
                if len(save) == 0:
                    return False
                flag = False
                if s[i] == ')' and save[-1] == '(':
                    save.pop()
                    flag = True
                elif s[i] == '}' and save[-1] == '{':
                    save.pop()
                    flag = True
                elif s[i] == ']' and save[-1] == '[':
                    save.pop()
                    flag = True
                else:
                    return flag
        return not save