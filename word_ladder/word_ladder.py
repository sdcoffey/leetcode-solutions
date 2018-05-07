from Queue import Queue

def wordDist(a, b):
    dist = abs(len(b) - len(a)) 

    for i in xrange(min(len(a), len(b))):
        if a[i] != b[i]:
            dist += 1

    return dist


class Graph(object):

    def __init__(self, word, children):
        self.word = word
        self.children = children
        self.pred = None

    def __str__(self):
        return '{} -> {}'.format(self.word, [n.word for n in self.children])


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


def buildGraph(beginWord, wordList, visited):
    node = Graph(beginWord, set())
    visited[beginWord] = node

    children = set([otherword for otherword in wordList if otherword != beginWord
                and wordDist(beginWord, otherword) == 1])

    for child in children:
        if child in visited:
            node.children.add(visited[child])
        else:
            node.children.add(buildGraph(child, wordList, visited))

    return node

class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []

        tree = buildGraph(beginWord, wordList, visited={})

        delta = 8

        paths = dfs(tree, endWord)
        paths = [path for path in paths if path[len(path) - 1] == endWord]

        if len(paths) > 0:
            paths = sorted(paths, key=lambda x: len(x))

            minLen = len(paths[0])

            return [l for l in paths if len(l) == minLen]

        return []


