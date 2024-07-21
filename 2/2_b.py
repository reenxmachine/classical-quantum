# Ryan McShane

import numpy
import math
from qiskit import *
from qiskit import BasicAer

# Implement (A (+) B) (+) C
'''
Truth Table
3 | 2 1 0

R | A B C
0 | 0 0 0
1 | 1 0 0
1 | 0 1 0
1 | 0 0 1
0 | 1 1 0
0 | 0 1 1
0 | 1 0 1
1 | 1 1 1
'''

# Quantum wires
q = QuantumRegister(11, 'q')
# Classical wires
c = ClassicalRegister(4, 'c')
#Build circuit
circ = QuantumCircuit(q, c)

# Inputs
#circ.x(q[0]) #A
#circ.x(q[1]) #B
circ.x(q[6]) #C

#Wire assignments
'''
q[0] = A
q[1] = B
q[2] = R1
q[3] = At
q[4] = Bt
q[5] = A (+) B
q[6] = C
q[7] = r1
q[8] = at
q[9] = bt
q[10] = (A (+) B) (+) C
'''

# Circuit
circ.barrier(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7],q[8], q[9], q[10])
circ.ccx(q[0], q[1], q[2])
circ.x(q[2]) # First NAND Gate comparing A and B

circ.ccx(q[0], q[2],q[3])
circ.x(q[3]) # Second NAND Gate comparing C and A

circ.ccx(q[2], q[1], q[4])
circ.x(q[4]) # Third NAND Gate comparing C and B

circ.ccx(q[3], q[4], q[5])
circ.x(q[5]) # Fourth and Final NAND Gate comparing At and Bt

circ.ccx(q[5], q[6], q[7]) #q[6] = C
circ.x(q[7]) # First NAND Gate comparing R1 and C

circ.ccx(q[5], q[7], q[8])
circ.x(q[8])

circ.ccx(q[6], q[7], q[9])
circ.x(q[9])

circ.ccx(q[8], q[9], q[10])
circ.x(q[10])

#undo


# Measure
circ.barrier(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10])
circ.measure(q[0], c[2]) #A
circ.measure(q[1], c[1]) #B
circ.measure(q[6], c[0]) #C
circ.measure(q[10], c[3]) #R

#Text Representation
text = circ.draw(output='text')
print(text)

#Test and Results
backend_sim = BasicAer.get_backend('qasm_simulator')
job_sim = execute(circ,backend_sim, shots=2048)
result_sim = job_sim.result()
counts = result_sim.get_counts()
print(counts)








