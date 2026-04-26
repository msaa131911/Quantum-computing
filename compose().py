#compose()
#একটা circuit-এর সাথে আরেকটা circuit যুক্ত করা
#Circuit A + Circuit B = Combined Circuit
from qiskit import QuantumCircuit

qc1 = QuantumCircuit(4)
for i in range(qc1.num_qubits):
    qc1.h(i)

qc2 = QuantumCircuit(4)
for j in range(qc2.num_qubits):
    qc2.s(j)

qc = qc1.compose(qc2)

qc.draw()