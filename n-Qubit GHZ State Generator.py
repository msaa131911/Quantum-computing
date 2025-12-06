#n-Qubit GHZ State Generator
#n-qubit GHZ (Greenberger–Horne–Zeilinger) state
from qiskit import QuantumCircuit

def GHZ_state(n):
  qc = QuantumCircuit(n)
  qc.h(0)

  for i in range(n-1):
    qc.cx(i, i+1)

  return qc
n=10
qc =GHZ_state(n)
qc.draw()