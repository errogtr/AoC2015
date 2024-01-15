def exec(registers):
    current = 0
    while True:
        name, *args = instructions[current].replace(",", "").split()
        match name:
            case "hlf":
                registers[args[0] == "b"] /= 2
            case "tpl":
                registers[args[0] == "b"] *= 3
            case "inc":
                registers[args[0] == "b"] += 1
            case "jmp":
                current += int(args[0]) - 1
            case "jie":
                if registers[args[0] == "b"] % 2 == 0:
                    current += int(args[1]) - 1
            case "jio":
                if registers[args[0] == "b"] == 1:
                    current += int(args[1]) - 1
        current += 1
        if current == len(instructions):
            return registers[1]


with open("data") as f:
    instructions = f.read().splitlines()

# ==== PART 1 ====
print(exec([0, 0]))

# ==== PART 2 ====
print(exec([1, 0]))
