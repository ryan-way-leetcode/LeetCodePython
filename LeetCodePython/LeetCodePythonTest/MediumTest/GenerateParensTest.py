import unittest
import timeit
from Medium.GenerateParens import Solution

class Test_ThreeSum(unittest.TestCase):
    
    def test_Example(self):
        solution = Solution()
        n = 3
        exp = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        actual = solution.generateParenthesis(n)

        for i in exp:
            self.assertTrue(i in actual)
        self.assertEqual(len(actual), len(exp))

    def test_Empty(self):
        solution = Solution()
        n = 0
        exp = []
        actual = solution.generateParenthesis(n)

        for i in exp:
            self.assertTrue(i in actual)
        self.assertEqual(len(actual), len(exp))

    def test_one(self):
        solution = Solution()
        n = 1
        exp = ["()"]
        actual = solution.generateParenthesis(n)

        for i in exp:
            self.assertTrue(i in actual)
        self.assertEqual(len(actual), len(exp))


if __name__ == '__main__':

    unittest.main()