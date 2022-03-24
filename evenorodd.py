import unittest

def check_EvenorOdd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

class Mycheck(unittest.TestCase):

    def test_case_checkvenorodd1(self):
        result = check_EvenorOdd(2)
        self.assertEqual("even",result)

    def test_case_checkevenorodd2(self):
        result = check_EvenorOdd(7)
        self.assertEqual("odd",result)

if __name__ == "__main__":
    unittest.main()