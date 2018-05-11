from word_dist import wordDist

class Node(object):

    def __init__(self, word, children):
        self.word = word
        self.children = children

    def __str__(self):
        return '{} -> {}'.format(self.word, [n.word for n in self.children])


def buildGraph(beginWord, wordList, visited):
    node = Node(beginWord, set())
    visited[beginWord] = node

    children = set([otherword for otherword in wordList if otherword != beginWord
                and wordDist(beginWord, otherword) == 1])

    for child in children:
        if child in visited:
            node.children.add(visited[child])
        else:
            node.children.add(buildNode(child, wordList, visited))

    return node

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
