import unittest

from valid_number import Solution

class TestValidNumber(unittest.TestCase):

    def testValidNumber(self):
        table = {
                '0': True,
                ' 0.1 ': True,
                'abc': False,
                '1 a': False,
                '2e10': True,
                '.1': True,
                '-1': True,
                '3.': True,
                '2e0': True,
                '-1.': True,
                '': False,
                ' ': False,
                '46.e3': True,
                '.2e81': True,
                'e9': False,
                ' 005047e+6': True,
                }

        s = Solution()

        for input, expected in table.iteritems():
            output = s.isNumber(input)
            self.assertEquals(expected, output, 'Input: {}, expected: {}, got: {}'.format(input, expected, output))
