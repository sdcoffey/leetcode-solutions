def wordDist(a, b):
	dist = abs(len(b) - len(a))

	for i in xrange(min(len(a), len(b))):
		if a[i] != b[i]:
			dist += 1

	return dist

def buildDistances(wordList):
	distances = {}

	for word in wordList:

		if word not in distances:
			distances[word] = {}

		for other in [other for other in wordList if other != word]:
			distances[word][other] = wordDist(word, other)

	return distances

class Solution(object):

	def findLadders(self, start, end, wordList):
		cp = [start]
		cp.extend(wordList)

		weighted_graph = buildDistances(cp)

	   # We always need to visit the start
		nodes_to_visit = {start}
		visited_nodes = set()
		# Distance from start to start is 0
		distance_from_start = {start: 0}
		tentative_parents = {}

		while nodes_to_visit:
			# The next node should be the one with the smallest weight
			current = min(
					[(distance_from_start[node], node) for node in nodes_to_visit]
					)[1]

			# The end was reached
			if current == end:
				break

			nodes_to_visit.discard(current)
			visited_nodes.add(current)

			edges = weighted_graph[current]
			unvisited_neighbours = set(edges).difference(visited_nodes)
			for neighbour in unvisited_neighbours:
				neighbour_distance = distance_from_start[current] + \
						edges[neighbour]
				if neighbour_distance < distance_from_start.get(neighbour,
						float('inf')):
					distance_from_start[neighbour] = neighbour_distance
					tentative_parents[neighbour] = current
					nodes_to_visit.add(neighbour)

		return _deconstruct_path(tentative_parents, end)


def _deconstruct_path(tentative_parents, end):
	if end not in tentative_parents:
		return None
	cursor = end
	path = []
	while cursor:
		path.append(cursor)
		cursor = tentative_parents.get(cursor)
	return list(reversed(path))
