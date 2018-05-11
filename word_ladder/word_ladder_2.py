def buildGraphHash(beginWord, wordList, resHash={}):
    if beginWord in resHash:
        return resHash

    node = Node(beginWord, set())

    kiddos = set([otherword for otherword in wordList if otherword != beginWord
                and wordDist(beginWord, otherword) == 1])

    resHash[beginWord] = kiddos

    for kiddo in kiddos:
        buildGraphHash(kiddo, wordList, resHash)

    return resHash

def wordDist(a, b):
    dist = abs(len(b) - len(a))

    for i in xrange(min(len(a), len(b))):
        if a[i] != b[i]:
            dist += 1

    return dist

class Solution(object):

    def findLadders(self, start, end, wordList):
        graphHash = buildGraphHash(start, wordList, {})

        paths = self.dfs(graphHash, start, end)

        return paths

    def dfs(self, graph, start, end):
        path = [start]
        stack = [(start, path)]

        min_length = float('inf')
        paths = []
        while stack:
            node, current_path = stack.pop()

            if len(current_path) > min_length:
                continue

            eligible_kiddos = [k for k in graph[node] if k not in current_path]

            for kiddo in eligible_kiddos:
                if kiddo == end:
                    current_path.append(kiddo)
                    if len(current_path) < min_length:
                        min_length = len(current_path)

                    paths.append(current_path)
                else:
                    kiddo_path = current_path + [kiddo]
                    stack.append((kiddo, kiddo_path))

        return [p for p in paths if len(p) == min_length]
