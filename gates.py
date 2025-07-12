from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
import numpy as np

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

def array_to_latex(matrix):
    """
    Convert a NumPy matrix to a LaTeX-formatted bmatrix string.
    """
    latex = "\\begin{bmatrix}"
    for i, row in enumerate(matrix):
        latex += " & ".join([str(int(el)) for el in row])
        if i != matrix.shape[0] - 1:
            latex += " \\\\ "
    latex += "\\end{bmatrix}"
    return latex



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



def get_initial_state():
    # |0⟩ state
    return np.array([[1], [0]])

def get_h_gate_matrix():
    return (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

def get_x_gate_matrix():
    return np.array([[0, 1], [1, 0]])

def get_y_gate_matrix():
    # Pauli-Y has imaginary components
    return np.array([[0, -1j], [1j, 0]])

def get_z_gate_matrix():
    return np.array([[1, 0], [0, -1]])

def get_s_gate_matrix():
    # S gate is a phase gate with imaginary component
    return np.array([[1, 0], [0, 1j]])

def get_t_gate_matrix():
    # T gate has a complex exponential
    return np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])


'''
# Get the statevector.
state = Statevector.from_instruction(qc)

plot_bloch_multivector(state.data)
plt.show()

#Test
qc.draw("mpl")
'''


