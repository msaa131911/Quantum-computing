from qiskit import QuantumCircuit 
qc = QuantumCircuit(2,2)   # 2 qubit, 2 classical
qc.h(0)                    # 0 নং qubit এ Hadamard
qc.cx(0,1)                 # CNOT 0->1
qc.measure([0,1],[0,1])    # মাপা
print(qc)