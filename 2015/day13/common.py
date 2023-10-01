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


# Get a list of people and their happiness if they sat next to each person
def get_people(data: list[str]):
    people = []

    for split_line in [line.split() for line in data]:
        if not any(person["name"] == split_line[0] for person in people):
            people.append(
                {
                    "name": split_line[0],
                    "happiness": {
                        line.split()[-1].replace(".", ""): int(line.split()[3])
                        if line.split()[2] == "gain"
                        else -int(line.split()[3])
                        for line in data
                        if line.split()[0] == split_line[0]
                    },
                }
            )

    return people


# Get a list of the total happiness for every permutation of the list of people
def get_seating_order_happiness(people: list[dict]):
    total_happiness = []

    for i, seating_order in enumerate(
        get_permutations([person["name"] for person in people])
    ):
        total_happiness.append(0)

        for j in range(len(seating_order)):
            for person in people:
                if person["name"] == seating_order[j]:
                    total_happiness[i] += person["happiness"][
                        seating_order[j + 1 if j < len(seating_order) - 1 else 0]
                    ]
                elif (
                    person["name"]
                    == seating_order[j + 1 if j < len(seating_order) - 1 else 0]
                ):
                    total_happiness[i] += person["happiness"][seating_order[j]]

    return total_happiness
