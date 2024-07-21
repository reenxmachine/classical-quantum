import numpy
import math
from qiskit import *
from qiskit import BasicAer

#Program NOR gate using X and CCX Gates
'''
NOR

1 | 0 0
0 | 0 1
0 | 1 0
0 | 1 1
''' Qu
#Quantum Wire
q = QuantumRegister(3, 'q')
#Classical Wire
c = ClassicalRegister(3, 'c')
#Build the Circuit
circ = QuantumCircuit(q,c)

#Inputs
circ.x(q[0])
#circ.x(q[1])

#Circuit
circ.barrier(q[0],q[1],q[2])
circ.x(q[0])
circ.x(q[1])
circ.ccx(q[0],q[1],q[2])

#Undo ~A ^ B
circ.x(q[0])
circ.x(q[1])

#Measure 
circ.barrier(q[0],q[1],q[2])
circ.measure(q[0], c[0])
circ.measure(q[1], c[1])
circ.measure(q[2], c[2])

#Picture Time
X = circ.draw(output="text")
print(X)

#Run an experiment
backend_sim = BasicAer.get_backend('qasm_simulator')
job_sim = execute(circ,backend_sim, shots=2048)
result_sim = job_sim.result()
counts = result_sim.get_counts()
print(counts)


