# z gate
from qiskit import QuantumCircuit
qc = QuantumCircuit(2,2)
qc.h(0)
qc.x(1)
qc.z(0) # z gate
qc.measure([0,1],[0,1])
qc.draw()


