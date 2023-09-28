from typing import Callable, Any


def update_lights(
    size: int, instructions: list, light_function: Callable[[str, int], Any]
):
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for instruction in instructions:
        instruction = instruction.replace("turn ", "").split()
        action = instruction[0]
        point1 = [int(coord) for coord in instruction[1].split(",")]
        point2 = [int(coord) for coord in instruction[3].split(",")]

        grid = [
            [
                light_function(action, grid[j][i])
                if point1[0] <= i <= point2[0]
                else grid[j][i]
                for i in range(len(grid[j]))
            ]
            if point1[1] <= j <= point2[1]
            else grid[j]
            for j in range(len(grid))
        ]

    return sum(map(sum, grid))
