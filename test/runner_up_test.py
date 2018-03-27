'''
Created on Mar 26, 2018

@author: faronr
'''
import unittest
import master.runner_up as ru


class Test(unittest.TestCase):


    def test_runner_up(self):
        rawinput = ["1 2 3 4 5 6 6"]
        result = ru.runner_up(rawinput)
        expected = 5
        self.assertEqual(expected, result, 
                         'Error: expected %s, recieved %s'% (str(expected),
                                                             str(result)))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()