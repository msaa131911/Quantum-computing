from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# Quantum Circuit: 1 qubit, 1 classical bit
qc = QuantumCircuit(1, 1)

# Step 1: Qubit কে superposition এ set করা
qc.h(0)

# Step 2: Measurement
qc.measure(0, 0)

# Simulator backend
simulator = AerSimulator()

# Run the circuit multiple times (simulate "time steps")
shots = 1000
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=shots).result()
counts = result.get_counts()

# Show counts (0 বা 1 এর frequency)
print(counts)

# Plotting
plt.bar(counts.keys(), counts.values())
plt.xlabel('Qubit State')
plt.ylabel('Counts')
plt.title('Quantum Clock Simulation')
plt.show()
