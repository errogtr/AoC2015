with open("data") as f:
    instructions = f.read()

# == PART 1 ==
print(instructions.count("(") - instructions.count(")"))


