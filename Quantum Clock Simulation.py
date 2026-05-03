from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

simulator = AerSimulator()
shots = 1000
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=shots).result()
counts = result.get_counts()
# Show count
print(counts)

plt.bar(counts.keys(), counts.values())
plt.xlabel('Qubit State')
plt.ylabel('Counts')
plt.title('Quantum Clock Simulation')
plt.show()
