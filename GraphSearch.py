###############
# Code Taken from: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
# Date Accessed: 02/10/2023
# License: None given
# Author: Valerio Velardo
###############
# CHANGELOG:
#   New main(), new graph
#   Modified the shortest path to return empty list if no path found
#   Modified the shortest path to return list with start if goal == start
###############

def friend_of_friend_finder(graph, entrant):
    print("Hi, {}!".format(entrant))
    # find friend to suggest
    for f in graph[entrant]:
        for ff in graph[f]:
            # check that this friend is not already direct friend
            if ff not in graph[entrant]:  # not already friends
                print("You should be friends with {0} because {1} is.".format(ff, f))
# end def friend_of_friend_finder(graph, entrant):


# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


# finds the shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return [start]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return []


# end bfs_shortest_path(graph, 'start', 'goal')


def main():
    # sample graph implemented as a dictionary
    graph = {'1': ['2', '3', '4'],
             '2': ['4', '5'],
             '3': ['6'],
             '4': ['5', '6', '7'],
             '5': ['4', '7'],
             '6': [],
             '7': ['6']}

    print(bfs_connected_component(graph, '6'))
# end def main():


if __name__ == "__main__":
    main()
