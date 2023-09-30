# Get cities and distances between each of them from the input
def get_cities_and_distances(routes: list):
    cities = []
    distances = []

    for route in [r.replace("to ", "").replace("= ", "").split() for r in routes]:
        if route[0] not in cities:
            cities.append(route[0])

        if route[1] not in cities:
            cities.append(route[1])

        route[2] = int(route[2])
        distances.append(route)

    return cities, distances


# Recursive function to get a list of all possible permutations of a list
def get_permutations(the_list: list, i: int = 0, permutations: list = None):
    length = len(the_list)

    if permutations is None:
        permutations = []

    if i == length:
        permutations.append(the_list.copy())
    else:
        for j in range(i, length):
            the_list[i], the_list[j] = the_list[j], the_list[i]
            get_permutations(the_list, i + 1, permutations)
            the_list[i], the_list[j] = the_list[j], the_list[i]

    return permutations


# Get total distances for each route
def get_total_distances(data: list):
    cities, distances = get_cities_and_distances(data)
    routes = get_permutations(cities)
    total_distances = []

    for route in routes:
        total_distances.append(0)

        for i in range(len(route) - 1):
            for distance in distances:
                if route[i] in distance and route[i + 1] in distance:
                    total_distances[-1] += distance[-1]

    return total_distances
