# wtp to test to find largest number among 2 numbers
import unittest

def largest(x,y):
    if x > y :
        return True
    else:
        return False

class checklargest(unittest.TestCase):

    def test_case_largest1(self):
        a = 20
        b = 10
        c =largest(a,b)
        self.assertTrue(c)

    def test_case_largest2(self):
        a = 10
        b = 20
        c =largest(a,b)
        self.assertFalse(c)


if __name__ == "__main__":
    unittest.main()