def wordDist(a, b):
    dist = abs(len(b) - len(a))

    for i in xrange(min(len(a), len(b))):
        if a[i] != b[i]:
            dist += 1

    return dist
