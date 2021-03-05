import unittest

import fizzbuzz

# I assume you want fizzbuzz to output to the command line,
# so we need to import some stuff to capture stdout
import sys
from io import StringIO

class FizzBuzzTestCase(unittest.TestCase):

    

    def catchSplitStdout(self):

        # Setup stdout capturing
        realStdout = sys.stdout
        sys.stdout = StringIO()

        # Call function
        fizzbuzz.fizzbuzz()

        # Get output and reset stdout
        output = sys.stdout.getvalue()
        lines = ["0"] + output.split() # The zero here is to make it 1 indexed
                                       # I do that here so index==number printed
        sys.stdout.close()
        sys.stdout = realStdout

        return lines
        
    def testBasic(self):
        # Tests that the code correct prints numbers that aren't multiples of 3 or 5
        
        lines = self.catchSplitStdout()

        self.assertEqual("1", lines[1])
        self.assertEqual("2", lines[2])
        self.assertEqual("29", lines[29])
        self.assertEqual("91", lines[91])

    def testFizz(self):
        # Tests that multiples of 3 that aren't multiples of 5 print Fizz

        lines = self.catchSplitStdout()

        self.assertEqual("Fizz", lines[3])
        self.assertEqual("Fizz", lines[6])
        self.assertEqual("Fizz", lines[27])
        self.assertEqual("Fizz", lines[99])
        
    def testBuzz(self):
        # Tests that multiples of 5 that aren't multiples of 3 print Buzz

        lines = self.catchSplitStdout()

        self.assertEqual("Buzz", lines[5])
        self.assertEqual("Buzz", lines[10])
        self.assertEqual("Buzz", lines[25])
        self.assertEqual("Buzz", lines[55])

    def testFizzBuzz(self):
        # Tests that FizzBuzz is printed for multiples of 3 and 5

        lines = self.catchSplitStdout()

        self.assertEqual("FizzBuzz", lines[15])
        self.assertEqual("FizzBuzz", lines[30])
        self.assertEqual("FizzBuzz", lines[75])
        self.assertEqual("FizzBuzz", lines[90])

if __name__ == "__main__":
    unittest.main()
