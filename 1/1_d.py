import numpy
import math
from qiskit import *
from qiskit import BasicAer

# Program XOR using Quantum Gates
'''
XNOR
1 | 0 0
0 | 0 1
0 | 1 0
1 | 1 1
'''

#Quantum Wires
q = QuantumRegister(6, 'q')
#Classical Wires
c = ClassicalRegister(3, 'c')
#Build Circuit
circ = QuantumCircuit(q,c)

#Inputs
circ.x(q[0])
circ.x(q[1])

#Wire assignments
'''
q[0] = A
q[1] = B
q[2] = C
q[3] = At(emp)
q[4] = Bt(emp)
q[5] = R(esult)
'''
#Circuit
circ.barrier(q[0], q[1], q[2])
circ.ccx(q[0], q[1], q[2])
circ.x(q[2]) # First NAND Gate comparing A and B

circ.ccx(q[0], q[2],q[3])
circ.x(q[3]) # Second NAND Gate comparing C and A

circ.ccx(q[2], q[1], q[4])
circ.x(q[4]) # Third NAND Gate comparing C and B

circ.ccx(q[3], q[4], q[5])
#circ.x(q[5]) # Fourth and Final NAND Gate comparing At and Bt

#Measure 
circ.barrier(q[0],q[1],q[2],q[3],q[4],q[5])
circ.measure(q[0], c[0])
circ.measure(q[1], c[1])
circ.measure(q[5], c[2])

#Text Representation
text = circ.draw(output='text')
print(text)

#Test and Results
backend_sim = BasicAer.get_backend('qasm_simulator')
job_sim = execute(circ,backend_sim, shots=2048)
result_sim = job_sim.result()
counts = result_sim.get_counts()
print(counts)



