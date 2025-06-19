from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector

#Later to be integrated via streamlit. Asking for user input.
#number_of_qubits = int(input("How many qubits do you wish to play with? "))

#To be made more dynamic after addition of streamlit. But set to 0 for the initial testing phase.

# Creating an initial circuit of one qubit. I plan to modify this later to allow the user to build a circuit 
# of their choice with multiple qubits.
#qc = QuantumCircuit(1)


#Functions for applying the gate utilites to the user's gate of choice. 
def h_gate(qc, qubit=0):
    '''
    Apply the hadamard gate.
    '''
    qc.h(qubit)
    return

def not_gate(qc, qubit=0):
    qc.x(qubit)
    return

def y_gate(qc, qubit=0):
    qc.y(qubit)
    return

def z_gate(qc, qubit=0):
    qc.z(qubit)
    return

def s_gate(qc, qubit=0):
    qc.s(qubit)
    return

def t_gate(qc, qubit=0):
    qc.t(qubit)
    return

def c_not_gate(qc, qubit=0):
    return




'''
# Get the statevector.
state = Statevector.from_instruction(qc)

plot_bloch_multivector(state.data)
plt.show()

#Test
qc.draw("mpl")
'''


