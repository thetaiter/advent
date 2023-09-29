def get_wire_signals(instructions):
    wires = {}
    finished_wires = {}

    for instruction in instructions:
        instruction = instruction.split(" -> ")
        signal = instruction[0].split()
        output = instruction[1]

        if len(signal) == 1 and signal[0].isdigit():
            finished_wires[output] = int(signal[0])
        else:
            wires[output] = signal

            if len(signal) == 3:
                if signal[0].isdigit():
                    wires[output][0] = int(signal[0])

                if signal[2].isdigit():
                    wires[output][2] = int(signal[2])

    while wires:
        for name, logic in wires.copy().items():
            if len(logic) == 1:  # Items with direct wire/signal connection
                if logic[0] in finished_wires:
                    finished_wires[name] = finished_wires[logic[0]]
                    del wires[name]
            elif len(logic) == 2:  # NOT logic gates
                if logic[1] in finished_wires:
                    finished_wires[name] = ~finished_wires[logic[1]]
                    del wires[name]
            elif len(logic) == 3:  # Other logic gates
                if logic[0] in finished_wires:
                    wires[name][0] = int(finished_wires[logic[0]])

                if logic[2] in finished_wires:
                    wires[name][2] = int(finished_wires[logic[2]])

                if isinstance(wires[name][0], int) and isinstance(wires[name][2], int):
                    if logic[1] == "AND":
                        finished_wires[name] = wires[name][0] & wires[name][2]
                    elif logic[1] == "OR":
                        finished_wires[name] = wires[name][0] | wires[name][2]
                    elif logic[1] == "RSHIFT":
                        finished_wires[name] = wires[name][0] >> wires[name][2]
                    elif logic[1] == "LSHIFT":
                        finished_wires[name] = wires[name][0] << wires[name][2]

                    del wires[name]

    return finished_wires
