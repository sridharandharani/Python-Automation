import unittest #import

class Testmyapp(unittest.TestCase): #create a class and pass unittest.Testcase

    def test_case1(self): #def testcase and testcase name must begin with test or test_
        pass

    def test_case2(self):
        pass

class myapp(unittest.TestCase): #we can create multiple classes
    def test_case3(self):
        pass

if __name__ == "__main__": #basic syntax for testing
    unittest.main()