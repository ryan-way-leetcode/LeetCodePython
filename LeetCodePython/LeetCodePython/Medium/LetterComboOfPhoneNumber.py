class Solution:
    
    numToLetters = [
            [], #dummy value
            [],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
            []
        ]

    def letterCombinations(self, digits: str):
        #base cases
        if len(digits) == 0: return []
        if len(digits) == 1: return self.numToLetters[int(digits[0])]
        
        retVal = []
        for i in reversed(digits):
            #first iteration
            if len(retVal) == 0:
                retVal = self.numToLetters[int(i)]
            else:
                list = []
                for j in self.numToLetters[int(i)]:
                    for k in retVal:
                        list.append(j + k)
                retVal = list
        return retVal

    #very pythony version
    def letterCombo_pythony(self, digits: str):
        #base cases
        if len(digits) == 0: return []
        if len(digits) == 1: return self.numToLetters[int(digits[0])]
        
        retVal = []
        for i in reversed(digits):
            #first iteration
            if len(retVal) == 0:
                retVal = self.numToLetters[int(i)]
            else:
                a = self.numToLetters[int(i)]
                #if these two lists are not generate at the same time
                #then the output will be incorrect
                a, retVal = [a[i//len(retVal)] for i in range(len(a)*len(retVal))], retVal*len(a)
                retVal = [i+j for i,j in zip(a,retVal)]
        return retVal


    

