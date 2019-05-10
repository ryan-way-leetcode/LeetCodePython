import unittest
from Easy.LetterComboOfPhoneNumber import Solution

class Test_LetterComboOfPhoneNumberTest(unittest.TestCase):
    
    def test_SingleDigit(self):
        digits = "9"
        solution = Solution()
        actual = solution.letterCombinations(digits)
        exp = ["w", "x", "y", "z"]
        self.assertEqual(actual, exp)

    def test_Example(self):
        digits = "23"
        solution = Solution()
        actual = solution.letterCombinations(digits)
        exp = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

        self.assertEqual(actual, exp)

    def test_Empty(self):
        digits = ""
        solution = Solution()
        actual = solution.letterCombinations(digits)
        exp = []

        self.assertEqual(actual, exp)

if __name__ == '__main__':
    unittest.main()
