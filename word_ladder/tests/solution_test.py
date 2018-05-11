import unittest

from word_ladder_2 import Solution

class TestCase(object):

    def __init__(self, begin, end, wordlist, expected):
        self.begin = begin
        self.end = end
        self.wordlist = wordlist
        self.expected = expected


class TestSolution(unittest.TestCase):

    def testSolution(self):
        cases = [
                TestCase('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], [
                    ['hit', 'hot', 'dot', 'dog', 'cog'],
                    ['hit', 'hot', 'lot', 'log', 'cog'],
                    ]),
                TestCase('a', 'c', ['a', 'b', 'c'], [
                    ['a', 'c'],
                    ]),
                TestCase("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"], [
                    ['a', 'c'],
                ]),
                ]

        s = Solution()

        for testCase in cases:
            self.assertEqual(testCase.expected, s.findLadders(testCase.begin, testCase.end, testCase.wordlist))
