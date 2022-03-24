import unittest

def divisibleby7(x):
    if x % 7 == 0:
        return True
    else:
        return False

class checkdivisible(unittest.TestCase):

    def test_case_check_div1(self):
        result = divisibleby7(14)
        self.assertTrue(result)

    def test_case_check_div2(self):
        result = divisibleby7(2)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()