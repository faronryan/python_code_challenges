'''
Created on Mar 26, 2018

@author: faronr
'''
import unittest
import python_code_challenges.leap_year_checker as lyc

class Test(unittest.TestCase):


    def testLeapYearChecker(self):
        rawinput = [1900]
        result = lyc.leap_year(rawinput) 
        expected = False
        self.assertEqual(expected, result, 
                         'Error: expected %s, recieved %s'% (str(expected),
                                                             str(result))) 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()