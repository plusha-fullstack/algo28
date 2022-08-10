import unittest
import unlock


class TestFunc(unittest.TestCase):

    def test_unlock(self):
        self.assertEqual(unlock.PatternUnlock(9,[1, 2, 3, 4, 5, 6, 2, 7, 8, 9]),'982843')
        self.assertEqual(unlock.PatternUnlock(6,[6,1,9,2,4,3,7]),'682843')
        self.assertEqual(unlock.PatternUnlock(2,[5,2,9]),'241421')
        self.assertEqual(unlock.PatternUnlock(7,[4,2,8,7,3,5,1,9]),'824264')
        self.assertEqual(unlock.PatternUnlock(6,[9,2,6,1,8,3,5]),'8717')






if __name__ == '__main__':
    unittest.main()
