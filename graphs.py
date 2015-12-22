import Queue
import collections


class Graph(object):

    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


class SquareGrid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0:
            results.reverse()  # legiable
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def __str__(self):
        lists = [[] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                lists[i].append('.')
        return "\n".join(' '.join(map(str, l)) for l in lists)


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        SquareGrid.__init__(self, width, height)
        self.weights = {}

    def cost(self, a, b):
        return self.weights.get(b, 1)



example_graph = Graph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}


def breadFirstSearch(graph, start, goal):
    frontier = Queue.Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            return current
            break

        #print('Visiting {}'.format(current))
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
    return visited
    
def dijkistraSearch(graph, start, goal):
    frontier = Queue.PriorityQueue()
    frontier.put(start, 0)
    come_from = {}
    cost_so_far = {}
    come_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            print 'Done'
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                come_from[next] = current 
    return come_from, cost_so_far


def reconstructPath(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path        


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def aStar(graph, start, goal):
    frontier = Queue.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            print 'Done'
            break


        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return cost_so_far, came_from 


g = GridWithWeights(4813, 4973)

#parents = breadFirstSearch(g, (741, 7), (2, 3))
#parent2 = dijkistraSearch(g, (87,2), (2,3))
parent3, parent3_dic = aStar(g, (741,2), (112, 545))
#print parents

#print len(parent2[1].keys())

print len(parent3_dic.keys())