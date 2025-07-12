import streamlit as st
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np


#END GOAL:
#When people stumble upon this app, i want them to leave with a basic understanding of quantum gates and bloch spheres, and the understanding that 
#quantum gates are not magical entities, rather, they are matrices that make differences in the state of the gate.
#I want them to also be able to undestand a bit about how ket 0 and ket 1 are vectors representing probabilities of the qubit to be in a particular state.
#FUTURE GOAL
#Make a full fledged quantum circuit builder where users can experiment with multiple qubits and gates and even combinations of gates.

##todo: help and expander info, initial state choice and vector multiplication to show transformation. 
#can i make the design more full size?
#the arrangement of the code is quite messy right now
#docstrings
#delete unnecessary libraries.


#Importing necessary gate apply and gate display funtions.
from gates import h_gate, not_gate, y_gate, z_gate, s_gate, t_gate, c_not_gate, array_to_latex
from display_utils import display_initial_state, display_h_gate, display_x_gate, display_y_gate, display_z_gate, display_s_gate, display_t_gate

#Tab configurations
st.set_page_config(
    page_title="Quantum Gates Playground",
    layout="wide",
    initial_sidebar_state="auto",
)

# App header and mini explanation
st.title("Your Very Own Quantum Playground")
st.subheader("The idea behind this project is to be able to produce a beginner-friendly space where you can tinker about and learn about quantum gate and quibits conceptually, mathematically and geometrically.")

#Expanders
#An expander to help the user understand qubits.
with st.expander("Click here to get an idea about qubits"):
    st.write('''
        A qubit is essentially a quantum bit. However, unlike the classical bit, qubits can exist not just as 0 or 1, but also in a *superposition* of 0 and 1.
        Essentially, the actual final value of a qubit is probabilistic unless a measurement is made.
    ''')

#An expander to help the user with the idea of quantum gates.
with st.expander("Click here to get an idea about quantum gates"):
    st.write('''
        A quantum gate is the quantum version of a logic gate from classical computing. Just like you can utilise a logic gate to change the state of a bit and produce the desired output, a quantum gate changes the state of a qubit (quantum bit).
    ''')


apply_button = st.button("Apply Gate")
column1, column2, column3 = st.columns(3)

#Test - all qubits set to 0, later give the user choice to choose initial qubit of choice.
#Leftmost column - Gate selection, display and explanation. 
with column1:
    st.header("Take your pick!")
    # Build a new circuit
    qc = QuantumCircuit(1)
    status = qc.draw(output="mpl")
    #st.pyplot(status)

    # Gate selection
    gate = st.selectbox("Choose a gate to apply:", ["H", "X", "Y", "Z", "S", "T"])

    # Apply the selected gate
    if apply_button:
        if gate == "H":
            h_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)
            with st.expander("ℹ️ H Gate"):
                st.write('''
                    The H gate or the Hadamard gate is 
                ''')
            
        elif gate == "X":
            not_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)  
            with st.expander("ℹ️ X Gate"):
                st.write('''
                    The X gate also known as the NOT gate or bit-flip function flips the state of the qubit. Eg, it changes the qubit 1 to 0 and qubit 0 to 1.
                ''') 

        elif gate == "Y":
            y_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)
            with st.expander("ℹ️ Y Gate"):
                st.write('''
                    The Y gate is 
                ''')

        elif gate == "Z":
            z_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)
            with st.expander("ℹ️ Z Gate"):
                st.write('''
                    The Z gate is 
                ''')

        elif gate == "S":
            s_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)
            with st.expander("ℹ️ S Gate"):
                st.write('''
                    An S gate is 
                ''')

        elif gate == "T":
            t_gate(qc, 0)
            with st.expander("ℹ️ T Gate"):
                st.write('''
                    The T gate is 
                ''')

#Centre Column - A glimpse of the actual algebra going on in the background.
with column2:
    st.header("The Maths")
    st.subheader("Initial State: Ket 0")
    display_initial_state()

    if apply_button:
        if gate == "H":
            st.subheader("H Gate Matrix")
            display_h_gate()
        elif gate == "X":
            st.subheader("X Gate Matrix")
            display_x_gate()
        elif gate == "Y":
            st.subheader("Y Gate Matrix")
            display_y_gate()
        elif gate == "Z":
            st.subheader("Z Gate Matrix")
            display_z_gate()
        elif gate == "S":
            st.subheader("S Gate Matrix")
            display_s_gate()
        elif gate == "T":
            st.subheader("T Gate Matrix")
            display_t_gate()   

    st.subheader("Final State")
    with st.expander("Learn more about how the final state is obtained"):
                st.write('''
                    The final state is obtained by multiplying the initial state vector with the gate matrix. The rules of matrix multiplication apply.
                ''')
    
     


#Rightmost Column - Visualization on the bloch sphere.
with column3:
    st.header("Bloch Sphere Visualization")
    # Show Bloch Sphere
    state = Statevector.from_instruction(qc)
    fig = plot_bloch_multivector(state.data)
    st.pyplot(fig)
