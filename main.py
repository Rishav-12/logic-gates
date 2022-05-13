class AndGate:
    def __init__(self):
        pass
    @staticmethod
    def evaluate(input1, input2):
        if input1 == 0 and input2 == 0:
            return 0
        if input1 == 0 and input2 == 1:
            return 0
        if input1 == 1 and input2 == 0:
            return 0
        if input1 == 1 and input2 == 1:
            return 1

class OrGate:
    def __init__(self):
        pass
    @staticmethod
    def evaluate(input1, input2):
        if input1 == 0 and input2 == 0:
            return 0
        if input1 == 0 and input2 == 1:
            return 1
        if input1 == 1 and input2 == 0:
            return 1
        if input1 == 1 and input2 == 1:
            return 1

class NotGate:
    def __init__(self):
        pass
    @staticmethod
    def evaluate(input1):
        if input1 == 0:
            return 1
        if input1 == 1:
            return 0

# Example circuit using combination
# of the three basic gates
gate1 = OrGate()
gate2 = NotGate()
gate3 = AndGate()
gate4 = OrGate()
inputs = [
    (0, 0, 0), (0, 0, 1),
    (0, 1, 0), (0, 1, 1),
    (1, 0, 0), (1, 0, 1),
    (1, 1, 0), (1, 1, 1)]

print("A | B | C | D | E | Q")
print("- " * 11)
for input in inputs:
    d = gate2.evaluate(gate1.evaluate(input[0], input[1]))
    e = gate3.evaluate(input[1], input[2])
    q = gate4.evaluate(d, e)

    print(f"{input[0]} | {input[1]} | {input[2]} | {d} | {e} | {q}")
