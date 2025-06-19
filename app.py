import streamlit as st
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

from gates import h_gate, not_gate, y_gate, z_gate, s_gate, t_gate, c_not_gate

column1, column2 = st.columns(2)

st.title("Quantum Playground")

#Test - all qubits set to 0
with column1:
    st.header("Take your pick!")
    # Build a new circuit
    qc = QuantumCircuit(1)

    # Gate selection
    gate = st.selectbox("Choose a gate to apply:", ["H", "X", "Y", "Z", "S", "T"])

    # Apply the selected gate
    if st.button("Apply Gate"):
        if gate == "H":
            h_gate(qc, 0)
        elif gate == "X":
            not_gate(qc, 0)
        elif gate == "Y":
            y_gate(qc, 0)
        elif gate == "Z":
            z_gate(qc, 0)
        elif gate == "S":
            s_gate(qc, 0)
        elif gate == "T":
            t_gate(qc, 0)


with column2:
    st.header("Bloch Sphere Visualization")
    # Show Bloch Sphere
    state = Statevector.from_instruction(qc)
    fig = plot_bloch_multivector(state.data)
    st.pyplot(fig)


