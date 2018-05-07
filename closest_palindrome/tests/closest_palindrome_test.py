import unittest

from closest_palindrome import Solution

class ClosestPalindromTest(unittest.TestCase):

    def testClosestPalindrome(self):
        table = {
                '123': '121',
                '101': '99',
                '1225': '1221',
                '13456': '13431',
                '0': '-1',
                '10': '9',
                '100': '101',
                '1213': '1221',
                '50': '55',
                '44': '44',
                '99': '101',
                '9989': '9999',
                '11': '9',
                '44': '33',
                '100': '99',
                '11911': '11811',
                '1119111': '1118111',
                '1331': '1221',
                }

        s = Solution()

        for input, expected in table.iteritems():
            self.assertEquals(expected, s.nearestPalindromic(input))

