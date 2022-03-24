import unittest

def add(x,y):     #def a function to check
    return x+y

class myapp(unittest.TestCase):

    def test_case_add(self):
        a =10
        b = 2
        c = add(a,b) # call the func
        self.assertEqual(a+b,c)

    def test_case_add2(self):
        a = 10.3
        b = 12.6
        c = add(a,b)
        self.assertEqual(a+b,c)

    def test_case_add3(self):
        a = -12
        b = -6
        c = add(a,b)
        self.assertEqual(a+b,c)

if __name__ == "__main__":
    unittest.main()