# Ryan McShane
# Logic Gates Modules

# AND, OR, XOR, NAND, NOR, XNOR
def AND(circuit, q, A, B, result):
    circuit.ccx(q[A], q[B], q[result])

def OR(circuit, q, A, B, result):
    circuit.x(q[A])
    circuit.x(q[B])
    circuit.ccx(q[result])
    circuit.x(q[result])

    circuit.x(q[B])
    circuit.x(q[A])


def NAND(circuit, q, A, B, result):
    circuit.ccx(q[A], q[B], q[result])
    circuit.x(q[result])


def NOR(circuit, q, A, B, result):
    circuit.x(q[A])
    circuit.x(q[B])
    circuit.ccx(q[result])
    # Undo
    circuit.x(q[B])
    circuit.x(q[A])


def XOR(circuit, q, A, B, result, t1, t2, t3):
    NAND(circuit, q[A], q[B], q[t1])
    circuit.x(q[t1])
    NAND(circuit, q[A], q[t1], q[t2])
    circuit.x(q[t2])
    NAND(circuit, q[B], q[t1], q[t3])
    circuit.x(q[t3])
    NAND(circuit, q[t2], q[t3], q[result])
    circuit.x(q[result])
    # Undo
    circuit.x(q[t3])
    NAND(circuit, q[B], q[t1], q[t3])
    circuit.x(q[t2])
    NAND(circuit, q[A], q[t1], q[t2])
    circuit.x(q[t1])
    NAND(circuit, q[A], q[B], q[t1])


def XNOR(circuit, q, a, b, result, R, At, Bt):
    # circuit, q = quantum register, a, b, result, R = first NAND, At=second NAND, Bt = third NAND
    XOR(circuit, a, b, result, R, At, Bt)
    circuit.x(q[result]) # Just XOR negated
