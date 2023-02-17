import unittest
import exercises as e

class ExerciseTest(unittest.TestCase):

    def test_exercise1(self):
        test1 = e.exercise1([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10)
        test2 = e.exercise1([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 12, 10)
        test3 = e.exercise1(([15, 8, 8, 2, 6, 4, 1, 7]), 2, 8)

        self.assertEqual(test1, 5)
        self.assertEqual(test2, 1)
        self.assertEqual(test3, 2)

    def test_exercise2(self):
        test1 = e.exercise2([3, 5], [3, 5, 6], [1, 2, 3, 4, 5, 6])
        test2 = e.exercise2([3, 5], [3, 5], [3, 5])
        test3 = e.exercise2([3, 5], [3, 5, 7], [1, 2, 3, 4, 5, 6])
        test4 = e.exercise2([3, 5], [3, 6], [1, 2, 3, 4, 5, 6])

        self.assertEqual(test1, True)
        self.assertEqual(test2, False)
        self.assertEqual(test3, False)
        self.assertEqual(test4, False)

    def test_exercise3(self):
        input = [1, 2, 3, 4, 5]
        output = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],[4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
        self.assertEqual(e.exercise3(input), output)

if __name__ == '__main__':
    unittest.main()