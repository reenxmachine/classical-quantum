# Ryan McShane

from qiskit import *


def conjunction(circuit, q, L, R, T):
    # Implements X1 /\ X3 /\ X5 /\ X6 = X7

    circuit.ccx(q[0], q[1], q[T[0]])
    tIndex = 0
    lIndex = 2
    circuit.barrier(q)
    while lIndex < (len(L)-1):
        circuit.ccx(q[L[lIndex]], q[T[tIndex]], q[T[tIndex+1]])
        lIndex += 1
        tIndex += 1
        circuit.barrier(q)
    circuit.ccx(q[L[lIndex]], q[T[tIndex]], q[R])
    # Undo
    while lIndex > 2:
        lIndex -= 1
        tIndex -= 1
        circuit.ccx(q[L[lIndex]], q[T[tIndex]], q[T[tIndex+1]])
        circuit.barrier(q)
    circuit.ccx(q[0], q[1], q[T[0]])

def disjunction(circuit, q, L, R, T):
    circuit.x(q[0])
    circuit.x(q[1])
    circuit.ccx(q[0], q[1], q[T[0]])
    circuit.barrier(q)
    tIndex = 0
    lIndex = 2
    while lIndex < (len(L) - 1):
        circuit.x(q[L[lIndex]])
        circuit.ccx(q[L[lIndex]], q[T[tIndex]], q[T[tIndex + 1]])
        lIndex += 1
        tIndex += 1
        circuit.barrier(q)
    circuit.x(q[L[lIndex]])
    circuit.ccx(q[L[lIndex]], q[T[tIndex]], q[R])
    circuit.x(q[R])

    circuit.barrier(q)
    # Undo
    while lIndex > 2:
        lIndex -= 1
        tIndex -= 1
        circuit.ccx(q[L[lIndex]], q[T[tIndex]], q[T[tIndex + 1]])
        circuit.x(q[L[lIndex]])
        circuit.barrier(q)
    circuit.ccx(q[0], q[1], q[T[0]])
    circuit.x(q[1])
    circuit.x(q[0])
