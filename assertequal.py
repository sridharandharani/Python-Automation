import unittest

class Testmyapp(unittest.TestCase):

    def test_case1(self):
        self.assertEqual("hello","hello") #check wheather both are equal

    def test_case2(self):
        a = 10
        b = 2
        c  = a+b
        self.assertEqual(a+b,c)  #check wheather both are equal

class myapp(unittest.TestCase):
    def test_case3(self):
        self.assertNotEqual("hello","hai") #check wheather both are not equal

if __name__ == "__main__":
    unittest.main()