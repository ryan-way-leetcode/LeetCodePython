import unittest
import timeit
from Medium.NextPermutation import Solution

class Test_NextPermutation(unittest.TestCase):
    
    def test_Example1(self):
        input = [1,2,3]
        sol = Solution()
        exp = [1,3,2]
        sol.nextPermutation(input)

        self.assertEqual(exp, input)
        
    def test_Example2(self):
        input = [3,2,1]
        exp = [1,2,3]
        sol = Solution()
        sol.nextPermutation(input)

        self.assertEqual(exp, input)

    def test_Example3(self):
        input = [1,1,5]
        exp = [1,5,1]
        sol = Solution()
        sol.nextPermutation(input)

        self.assertEqual(exp, input)


if __name__ == '__main__':
    unittest.main()