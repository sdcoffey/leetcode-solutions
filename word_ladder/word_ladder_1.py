from Queue import Queue

from word_dist import wordDist
from node import Node, buildGraph


def dfs(root, end):
    return _dfs(root, end, set(), [], [])

def _dfs(root, end, visited, path, paths, minLen=100000):
    if len(path) > minLen:
        return

    if root.word in visited:
        return

    path.append(root.word)
    visited.add(root.word)

    for child in root.children:
        if child.word == end:
            path.append(child.word)
            paths.append(path)
            print path

            sorted(paths, key=lambda x: len(x))

            print minLen

            return

        elif len(path) + 1 <= minLen:
            minLen = 100000
            if len(paths) > 0:
                minLen = len(paths[0])

            _dfs(child, end, visited.copy(), path[:], paths, minLen)

    return paths


class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []

        tree = buildGraph(beginWord, wordList, visited={})

        paths = dfs(tree, endWord)
        paths = [path for path in paths if path[len(path) - 1] == endWord]

        if len(paths) > 0:
            paths = sorted(paths, key=lambda x: len(x))

            minLen = len(paths[0])

            return [l for l in paths if len(l) == minLen]

        return []


