import re


class Solution(object):

    def isPalindrome(self, n):
        lastIndex = len(n) - 1
        for i in range(lastIndex, (len(n)/2) - 1, -1):
            if n[i] != n[lastIndex - i]:
                return False

        return True


    def nearestPalindromic(self, n):
        n = n.strip()

        if int(n) <= 10:
            return str(int(n) - 1)
        elif re.match(r'^9+$', n):
            return str(int(n) + 2)
        elif re.match(r'10+', n):
            return str(int(n) - 1)
        elif self.isPalindrome(n):
            if n == '11':
                return '9'
            else:
                exp = len(n) - 2
                sub = 10*pow(10,exp)+1
                print 'subtracting {}'.format(sub)
                return self.nearestPalindromic(str(int(n) - sub))

        n = list(n)

        lastIndex = len(n) - 1
        for i in range(lastIndex, (len(n)/2) - 1, -1):
            n[i] = n[lastIndex - i]

        return ''.join(n)

