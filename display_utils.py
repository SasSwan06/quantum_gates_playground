import streamlit as st
import numpy as np

from gates import array_to_latex

#Gate Display Functions.
def display_initial_state(initial_choice):
    if initial_choice == "|0⟩":
        st.latex(r"\begin{bmatrix}1 \\ 0\end{bmatrix}")
    else:
        st.latex(r"\begin{bmatrix}0 \\ 1\end{bmatrix}")

def display_h_gate():
    '''
    Function to display a hadamard gate on streamlit interface.
    Converts pauli's H matrix to latex form for display.
    '''
    H = np.array([[1, 1], [1, -1]])
    latex_matrix = array_to_latex(H)
    st.latex(r"H = \frac{1}{\sqrt{2}}" + latex_matrix)

def display_x_gate():
    '''
    Function displays the matrix notation of NOT gate on streamlit interface.
    Converts pauli's X matrix to latex form for display.
    '''
    X = np.array([[0, 1], [1, 0]])
    latex_matrix = array_to_latex(X)
    st.latex(r"X = " + latex_matrix)

def display_y_gate():
    '''
    Function displays the matrix notation of Y gate on streamlit interface.
    Converts pauli's Y matrix to latex form for display.
    '''
    #Hardcoding the imaginary values.
    latex_matrix = r"\begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}"
    st.latex(r"Y = " + latex_matrix)

def display_z_gate():
    Z = np.array([[1, 0], [0, -1]])
    latex_matrix = array_to_latex(Z)
    st.latex(r"Z = " + latex_matrix)

def display_s_gate():
    latex_matrix = r"\begin{bmatrix} 1 & 0 \\ 0 & i \end{bmatrix}"
    st.latex(r"S = " + latex_matrix)

def display_t_gate():
    latex_matrix = r"\begin{bmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{bmatrix}"
    st.latex(r"T = " + latex_matrix)
