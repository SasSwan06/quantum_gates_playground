from qiskit import QuantumCircuit
from IPython.display import display
import matplotlib.pyplot as plt

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.s(0)
circuit.y(0)

display(circuit.draw(output="mpl"))
plt.show()