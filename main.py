import random

from GraphSearch import *


def shortest_route_finder(graph, location, destination, stop_over="none"):
    dict_of_routes = {'OMA': 'Omaha', 'SDF': 'Louisville', 'BWI': 'Baltimore-Washington', 'PWM': 'Portland',
                      'SLC': 'Salt Lake City', 'BZE': 'Belize City', 'DAL': 'Dalas', 'HOU': 'Houston', 'MDW': 'Chicago'}

    response = "The shortest route from {0} to {1} ".format(dict_of_routes[location],
                                                            dict_of_routes[destination])

    def printHelper(paths, resp):
        resp = resp
        for p in paths:
            if len(paths) >= 1:
                resp += dict_of_routes[p] + ", then to "
        resp += dict_of_routes[destination] + "."
        return resp
    #     end of def printHelper(paths, resp):

    if stop_over != "none":  # if there is a given stopover
        path1 = bfs_shortest_path(graph, location, stop_over)
        path = bfs_shortest_path(graph, path1[-1:][0], destination)
        result_path = path[1:-1]

        response += "with a layover in {0} is going from {1} to {0}, then to  ".format(
            dict_of_routes[stop_over],
            dict_of_routes[location],
            dict_of_routes[
                result_path[-1]])
        response = printHelper(result_path, response)

    else:  # without a stopover
        path = bfs_shortest_path(graph, location, destination)
        response += "is going from {0} to ".format(dict_of_routes[location])
        if len(path) <= 2:
            result_path = path[-1:]
        else:
            result_path = path[1:-1]
        response = printHelper(result_path, response)

    return response


def main():
    # sample graph implemented as a dictionary
    graph = {'OMA': ['MDW', 'HOU', 'DAL'],
             'SDF': ['MDW', 'BWI', 'DAL', 'HOU'],
             'BWI': ['MDW', 'SDF', 'HOU', 'DAL', 'SLC', 'PWM'],
             'PWM': ['MDW', 'BWI'],
             'SLC': ['MDW', 'BWI', 'HOU', 'DAL'],
             'BZE': ['HOU'],
             'DAL': ['HOU', 'SLC', 'OMA', 'MDW', 'SDF', 'BWI'],
             'HOU': ['BZE', 'BWI', 'SDF', 'MDW', 'OMA', 'DAL', 'SLC'],
             'MDW': ['PWM', 'BWI', 'SLC', 'OMA', 'SDF', 'DAL', 'HOU']}

    # shortest_route_finder(graph, location, destination, stop_over):

    # • I want to go from Omaha to Louisville.
    print(shortest_route_finder(graph, 'OMA', 'SDF'))
    print("...............................................")

    # • I want to go from Baltimore-Washington to Salt Lake City, then to Portland, ME.
    # shortest_route_finder(graph, location, destination, stop_over):
    print(shortest_route_finder(graph, 'BWI', 'PWM', 'SLC'))
    print("...............................................")

    # • I want to go from Belize City to Portland, ME
    print(shortest_route_finder(graph, 'BZE', 'PWM'))


# end def main():


if __name__ == "__main__":
    print("=================================================")
    main()
    print("=================================================")
