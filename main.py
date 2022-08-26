from queue import PriorityQueue


class point:
    def __init__(self, i, j, distance, path_via):
        self.index_i = i
        self.index_j = j
        self.dist = distance
        self.path = path_via

    def i(self):
        return self.index_i

    def j(self):
        return self.index_j

    def distance(self):
        return self.dist

    def get_path(self):
        return self.path

    # def min_value(self):
    # return self.min_val


def diak(map):
    distances_from_s = [[0 for x in range(0,len(map))] for x in range(0,len(map))]

    for i in range(len(map)):
        for j in range(len(map)):
            distances_from_s[i][j] = 999

    distances_from_s[0][0] = 0

    i, j = 0, 0
    unvisited_nodes = list(map)

    unvisited_nodes[i][j] = unvisited_nodes[i][j].upper()
    update(distances_from_s, unvisited_nodes)

    pq = []
    s = point(0, 0, 0, "null")
    pq.append(s)



    while len(pq) > 0:
        current_vertex = pq.pop(0)

        i = current_vertex.i()
        j = current_vertex.j()



        if unvisited_nodes[i][j] not in {"e","S","N"}:
            unvisited_nodes[i][j] = "_"
        else:
            unvisited_nodes[i][j] = unvisited_nodes[i][j].upper()

        if valid_node(i + 1, j, unvisited_nodes):
            if i < len(unvisited_nodes) - 1:
                if distances_from_s[i][j] + 1 < distances_from_s[i + 1][j]:
                    distances_from_s[i + 1][j] = distances_from_s[i][j] + 1
                    pq = append_by_distance(pq, point(i + 1, j, distances_from_s[i + 1][j], current_vertex))
            if j < len(unvisited_nodes) - 1:
                if distances_from_s[i][j] + 1 < distances_from_s[i][j + 1]:
                    distances_from_s[i][j + 1] = distances_from_s[i][j] + 1
                    pq = append_by_distance(pq, point(i, j + 1, distances_from_s[i][j + 1], current_vertex))
            if i < len(unvisited_nodes) - 1 and j < len(unvisited_nodes) - 1:
                if distances_from_s[i][j] + 1.5 < distances_from_s[i + 1][j + 1]:
                    if valid_node(i + 1, j+1, unvisited_nodes):
                        distances_from_s[i + 1][j + 1] = distances_from_s[i][j] + 1.5
                        pq = append_by_distance(pq, point(i + 1, j + 1, distances_from_s[i + 1][j + 1], current_vertex))

        elif valid_node(i, j + 1, unvisited_nodes):
            if i < len(unvisited_nodes) - 1:
                if distances_from_s[i][j] + 1 < distances_from_s[i + 1][j]:
                    distances_from_s[i + 1][j] = distances_from_s[i][j] + 1
                    pq = append_by_distance(pq, point(i + 1, j, distances_from_s[i + 1][j], current_vertex))
            if j < len(unvisited_nodes) - 1:
                if distances_from_s[i][j] + 1 < distances_from_s[i][j + 1]:
                    distances_from_s[i][j + 1] = distances_from_s[i][j] + 1
                    pq = append_by_distance(pq, point(i, j + 1, distances_from_s[i][j + 1], current_vertex))
            if i < len(unvisited_nodes) - 1 and j < len(unvisited_nodes) - 1:
                if distances_from_s[i][j] + 1.5 < distances_from_s[i + 1][j + 1]:
                    if valid_node(i+1, j + 1, unvisited_nodes):
                        distances_from_s[i + 1][j + 1] = distances_from_s[i][j] + 1.5
                        pq = append_by_distance(pq, point(i + 1, j + 1, distances_from_s[i + 1][j + 1], current_vertex))

        elif valid_node(i + 1, j + 1, unvisited_nodes):
            if i < len(unvisited_nodes)-1:
                if distances_from_s[i][j] + 1 < distances_from_s[i + 1][j]:
                    distances_from_s[i + 1][j] = distances_from_s[i][j] + 1
                    pq = append_by_distance(pq, point(i + 1, j, distances_from_s[i + 1][j], current_vertex))
            if j < len(unvisited_nodes)-1:
                if distances_from_s[i][j] + 1 < distances_from_s[i][j + 1]:
                    distances_from_s[i][j + 1] = distances_from_s[i][j] + 1
                    pq = append_by_distance(pq, point(i, j + 1, distances_from_s[i][j + 1], current_vertex))
            if i < len(unvisited_nodes)-1 and j < len(unvisited_nodes)-1:
                if distances_from_s[i][j] + 1.5 < distances_from_s[i + 1][j + 1]:
                    if valid_node(i + 1, j + 1, unvisited_nodes):
                        distances_from_s[i + 1][j + 1] = distances_from_s[i][j] + 1.5
                        pq = append_by_distance(pq, point(i + 1, j + 1, distances_from_s[i + 1][j + 1], current_vertex))




        update(distances_from_s, unvisited_nodes)

    via_i = current_vertex.get_path().i()
    via_j = current_vertex.get_path().j()


    while via_i + via_j > 0:
        unvisited_nodes[via_i][via_j] = "@"
        current_vertex = current_vertex.get_path()
        via_i = current_vertex.i()
        via_j = current_vertex.j()


    update(distances_from_s, unvisited_nodes)


def append_by_distance(pq, point):
    inserted = False
    for i in range(len(pq)):
        if point.dist < pq[i].dist:
            pq.insert(i,point)
            inserted = True
    if not inserted:
        pq.append(point)
    return pq


def valid_node(i, j, unvisited_nodes):



    if i > len(unvisited_nodes)-1 or j > len(unvisited_nodes)-1:
        return False
    if unvisited_nodes[i][j] == "N":
        return False
    elif unvisited_nodes[i][j] == '.':
        return True
    return False


def print_map(map, name):
    if name == 1:
        print("BASE MAP:")
    elif name == 2:
        print("DISTANCES FROM START:")
    elif name == 3:
        print("UNVISTIED NODES:")

    for i in range(len(map)):
        print(map[i])
    print()


def update(distances_from_s, unvisited_nodes):
    print("_________________________________")
    print_map(unvisited_nodes, 3)
   #print_map(distances_from_s, 2)

n = 3

map = [["." for x in range(0,n)] for x in range(0,n)]
map[0][0] = "s"
map[n-1][n-1] = "e"

map[1][1] = "N"



print_map(map, 1)

diak(map)
