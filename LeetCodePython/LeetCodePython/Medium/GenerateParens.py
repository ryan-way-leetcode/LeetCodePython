class Solution:
    def generateParenthesis(self, n):
        if n == 0: return []

        retVal = ["("*n+")"*n]
        for i in retVal:
            for j in range(1, len(i)-2):
                if i[j] == "(" and i[j+1] == ")":
                    newVal = i[:j] + ")(" + i[j+2:]
                    if newVal not in retVal and self.isvalidparens(newVal):
                        retVal.append(newVal)
        return retVal

    def isvalidparens(self, string):
        count = 0
        for i in string:
            count += 1 if i == "(" else -1
            if count < 0: return False
        return count == 0
