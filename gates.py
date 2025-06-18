from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector

#Later to be integrated via streamlit. Asking for user input.
number_of_qubits = int(input("How many qubits do you wish to play with? "))

#To be made more dynamic after addition of streamlit. But set to 0 for the initial testing phase.
initial_state = 0

# Create a new circuit with two qubits
qc = QuantumCircuit(number_of_qubits)
 
# Add a Hadamard gate to qubit of user's choice.
final_state = qc.h(initial_state)

#Test
qc.draw("mpl")
plt.show()
