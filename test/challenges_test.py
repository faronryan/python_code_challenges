'''
Created on Mar 26, 2018

@author: faronr
'''
import unittest
import python_code_challenges.challenges as pcc
import python_code_challenges.leap_year_checker as lyc
import python_code_challenges.runner_up as ru


class Test(unittest.TestCase):

    def testLeapYearChecker(self):
        rawinput = [1900]
        result = lyc.leap_year(rawinput) 
        expected = False
        self.assertEqual(expected, result, 
                         'Error: expected %s, recieved %s'% (str(expected),
                                                             str(result))) 

    def testRunnerUp(self):
        rawinput = ["1 2 3 4 5 6 6"]
        result = ru.runner_up(rawinput)
        expected = 5
        self.assertEqual(expected, result, 
                         'Error: expected %s, recieved %s'% (str(expected),
                                                             str(result)))
    
    def testFindPercentage(self):
        rawinput = [3,"Krishna 67 68 69","Arjun 70 98 63",
                    "Malika 52 56 60",'Malika']
        result = pcc.find_percentage(rawinput)
        expected = '56.00'
        self.assertEqual(expected, result, 
                         'Error: expected %s, recieved %s'% (str(expected),
                                                             str(result)))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()