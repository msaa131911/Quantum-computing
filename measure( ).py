from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)
qc.h(0)              # প্রথম কিউবিটে superposition
qc.x(1)              # দ্বিতীয় কিউবিটে X gate
qc.measure(0,0)   # দুই কিউবিট মাপা
qc.measure(1,1)   # দুই কিউবিট মাপা
qc.draw()
