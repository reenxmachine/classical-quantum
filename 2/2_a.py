#By Ryan McShane

import numpy
import math
from qiskit import *
from qiskit import BasicAer

# Implement (A ^ ~S) V (B ^ S)
'''
Truth Table
R | A S B
----------
0 | 0 0 0
1 | 1 0 0
0 | 0 1 0
0 | 0 0 1
0 | 1 1 0
1 | 1 0 1
1 | 0 1 1
1 | 1 1 1
'''

#Quantum Wires
q = QuantumRegister(6, 'q')
#Classical Wires
c = ClassicalRegister(4, 'c')
#Build Circit
circ = QuantumCircuit(q, c)

#Wire assignments
'''
q[0] = A
q[1] = S
q[2] = B
q[3] = Result of A ^ ~S
q[4] = Result of S ^ B
q[5] = Result of ~q[3] ^ ~q[4]
q[5] = Result of ~q[5]
'''

#Inputs
circ.x(q[0]) #A
#circ.x(q[1]) #S
#circ.x(q[2]) #B


# Implement (A ^ ~S) V (B ^ S)
#Circuit
circ.barrier(q[0], q[1], q[2], q[3], q[4], q[5])
circ.x(q[1]) # ~S
circ.ccx(q[0],q[1],q[3])# (A ^ ~S)
circ.x(q[1]) # undo ~S
circ.ccx(q[1], q[2], q[4])# (S ^ B)

circ.x(q[3]) # ~ (A ^ ~S)
circ.x(q[4]) # ~( S ^ B)
circ.ccx(q[3], q[4], q[5]) # ~q[5] ^ ~q[6]
circ.x(q[5]) # ~(~q[5] ^ ~q[6])

#Measure
circ.barrier(q[0],q[1],q[2],q[3],q[4],q[5])
circ.measure(q[0],c[0])
circ.measure(q[1],c[1])
circ.measure(q[2],c[2])
circ.measure(q[5],c[3])

#Picture Time
X = circ.draw(output="text")
print(X)

#Run Experiments
backend_sim = BasicAer.get_backend('qasm_simulator')
job_sim = execute(circ, backend_sim, shots=2048)
result_sim = job_sim.result()
counts = result_sim.get_counts()
print(counts)







