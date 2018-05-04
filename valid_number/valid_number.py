import re

class Solution(object):
    def isNumber(self, num):
        num = num.strip()

        if len(num) == 0:
            return False

        if num[0] == '-' or num[0] == '+':
            num = num[1:]

        if re.match(r'^\d+$', num):
            return True
        elif re.match(r'^(\d+)?\.\d+$', num):
            return True
        elif re.match(r'^\d+\.(\d+)?$', num):
            return True
        elif re.match(r'^\d+(\.)?(\d+)?e(\-|\+)?[0-9](\d+)?$', num):
            return True
        elif re.match(r'^(\d+)?(\.)?\d+e(\-|\+)?[0-9](\d+)?$', num):
            return True

        return False


