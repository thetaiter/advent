def get_sequence(this_iteration, num_iterations):
    for _ in range(num_iterations):
        next_iteration = ""

        for i in range(len(this_iteration)):
            if i != 0 and this_iteration[i] == this_iteration[i - 1]:
                continue

            number = this_iteration[i]
            number_of_number = 1

            while (
                i + number_of_number < len(this_iteration) - 1
                and this_iteration[i + number_of_number] == number
            ):
                number_of_number += 1

            next_iteration += f"{number_of_number}{number}"

        this_iteration = next_iteration

    return this_iteration
