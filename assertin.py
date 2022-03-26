import unittest

def mylist():
    list = ["1","3","5","sri",7]
    return list

class checklist(unittest.TestCase):

    def test_list1(self):
        element = "5"
        self.assertIn(element,mylist()) #checks wheather the element is in the list

    def test_list2(self):
        element = "6"
        self.assertNotIn(element,mylist()) #checks wheather the element not in the list

if __name__ == "__main__":
    unittest.main()