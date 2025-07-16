from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
import numpy as np

#Later to be integrated via streamlit. Asking for user input.
#number_of_qubits = int(input("How many qubits do you wish to play with? "))

#To be made more dynamic after addition of streamlit. But set to 0 for the initial testing phase.

# Creating an initial circuit of one qubit. I plan to modify this later to allow the user to build a circuit 
# of their choice with multiple qubits.
#qc = QuantumCircuit(1)


def array_to_latex(matrix):
    latex = r"\begin{bmatrix}"
    for row in matrix:
        latex_row = []
        for el in row:
            if np.iscomplex(el):
                real = el.real
                imag = el.imag
                if np.isclose(real, 0) and np.isclose(imag, 1):
                    latex_row.append("i")
                elif np.isclose(real, 0) and np.isclose(imag, -1):
                    latex_row.append("-i")
                elif np.isclose(real, 0):
                    latex_row.append(f"{imag:.2f}i")
                elif np.isclose(imag, 0):
                    latex_row.append(f"{real:.2f}")
                else:
                    sign = "+" if imag > 0 else "-"
                    latex_row.append(f"{real:.2f}{sign}{abs(imag):.2f}i")
            else:
                latex_row.append(f"{el:.2f}")
        latex += " & ".join(latex_row) + r"\\"
    latex += r"\end{bmatrix}"
    return latex


#Functions for applying the gate utilites to the user's gate of choice. 
def h_gate(qc, qubit=0):
    '''
    Apply the hadamard gate on a single qubit.
    '''
    qc.h(qubit)
    return


def not_gate(qc, qubit=0):
    '''
    Apply the X or NOT gate on a single qubit.
    '''
    qc.x(qubit)
    return

def y_gate(qc, qubit=0):
    '''
    Apply the Y gate on a single qubit.
    '''
    qc.y(qubit)
    return

def z_gate(qc, qubit=0):
    '''
    Apply the Z gate on a single qubit.
    '''
    qc.z(qubit)
    return

def s_gate(qc, qubit=0):
    '''
    Apply the S gate on a single qubit.
    '''
    qc.s(qubit)
    return

def t_gate(qc, qubit=0):
    '''
    Apply the T gate on a single qubit.
    '''
    qc.t(qubit)
    return

def get_initial_state(choice):
    '''
    Return an array (ket 0 or ket 1) of the initial state chosen by the user.
    '''
    #shorthand condition to return array according to chosen initial state.
    return np.array([[1], [0]]) if choice == "|0⟩" else np.array([[0], [1]])


def get_h_gate_matrix():
    '''
    Return an array of the H gate matrix.
    '''
    return (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

def get_x_gate_matrix():
    '''
    Return an array of the X gate matrix (Pauli's X).
    '''
    return np.array([[0, 1], [1, 0]])

def get_y_gate_matrix():
    '''
    Return an array of the Y gate matrix (Pauli's Y).
    '''
    # Pauli-Y has imaginary components
    return np.array([[0, -1j], [1j, 0]])

def get_z_gate_matrix():
    '''
    Return an array of the Z gate matrix (Pauli's Z).
    '''
    return np.array([[1, 0], [0, -1]])

def get_s_gate_matrix():
    '''
    Return an array of the S gate matrix.
    '''
    # S gate is a phase gate with imaginary component
    return np.array([[1, 0], [0, 1j]])

def get_t_gate_matrix():
    '''
    Return an array of the T gate matrix.
    '''
    # T gate has a complex exponential
    return np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])



