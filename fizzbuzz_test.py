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


        
        


if __name__ == "__main__":
    unittest.main()
