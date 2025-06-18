from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector

#Later to be integrated via streamlit. Asking for user input.
#number_of_qubits = int(input("How many qubits do you wish to play with? "))

#To be made more dynamic after addition of streamlit. But set to 0 for the initial testing phase.
initial_state = 0 #####

# Create a new circuit with two qubits
qc = QuantumCircuit(1)


# Add a Hadamard gate to qubit of user's choice.
qc.x(0)
#qc.h(0)

# Get the statevector.
state = Statevector.from_instruction(qc)

plot_bloch_multivector(state.data, title="Bloch Sphere via plot_bloch_multivector")
plt.show()

'''
#Test
qc.draw("mpl")
'''


