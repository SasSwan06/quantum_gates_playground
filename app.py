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
#docstrings
#NOTE: Currently, i am not storing session state, as it would require  me to change the way the matrices are displayed too. However, that is certainly a future goal.


#Importing necessary gate apply and gate display funtions.
from gates import h_gate, not_gate, y_gate, z_gate, s_gate, t_gate, array_to_latex, get_initial_state, get_h_gate_matrix, get_x_gate_matrix, get_y_gate_matrix, get_z_gate_matrix, get_s_gate_matrix, get_t_gate_matrix
from display_utils import display_initial_state, display_h_gate, display_x_gate, display_y_gate, display_z_gate, display_s_gate, display_t_gate

#Tab configurations
st.set_page_config(
    page_title="Quantum Gates Playground",
    layout="wide",
    initial_sidebar_state="auto",
)


# App header and mini explanation
st.markdown("<h1 style='text-align: center; font-size: 36px;'>Your Very Own Quantum Playground</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-size: 20px;'>Understand quantum gates conceptually, mathematically, and visually.</h3>", unsafe_allow_html=True)

#TOUR THE IDE - Work In Progress
# if "tour_step" not in st.session_state:
#     st.session_state.tour_step = 0

# steps = [
#     "Welcome to Quantum Playground!",
#     "Choose your initial qubit state using the dropdown.",
#     "Apply a quantum gate to see its effect.",
#     "View the updated qubit on the Bloch sphere.",
#     "That’s it! Enjoy exploring quantum logic."
# ]

# st.markdown(f"**Tour Step {st.session_state.tour_step + 1}:** {steps[st.session_state.tour_step]}")

# col1, col2 = st.columns([1, 3])
# with col1:
#     if st.button("Next ➡"):
#        if st.session_state.tour_step < len(steps) - 1:
#            st.session_state.tour_step += 1
#with col2:
#   if st.button("⏹ End Tour"):
#        st.session_state.tour_step = 0


#Expanders introducing key initial concepts.
#An expander to help the user understand qubits.
with st.expander("Click here to get an idea about qubits"):
    st.write('''
        A qubit is essentially a quantum bit. However, unlike the classical bit, qubits can exist not just as 0 or 1, but also in a superposition of 0 and 1.
        Essentially, the actual final value of a qubit is probabilistic unless a measurement is made.
    ''')

#An expander to help the user with the idea of quantum gates.
with st.expander("Click here to get an idea about quantum gates"):
    st.write('''
        A quantum gate is the quantum version of a logic gate from classical computing. Just like you can utilise a logic gate to change the state of a bit and produce the desired output, a quantum gate changes the state of a qubit (quantum bit).
    ''')

#An expander to help the user understand the bloch sphere.
with st.expander("Click here to get an idea about the bloch sphere."):
    st.write('''
        The Bloch sphere is a visual representation of a single qubit's state. It helps us understand how quantum gates transform the qubit, including changes in probability, phase, and orientation.
    ''')


#Allowing users to choose their initial state - only ket 0 or ket 1 for now.
st.subheader("Choose initial state:")
initial_choice = st.radio(
    "Choose initial state (hidden label)",
    ["|0⟩", "|1⟩"],
    label_visibility="collapsed",
    help="Pick the starting position of your qubit on the Bloch sphere."
)

#Initiating a column-like UI for the users.
column1, column2, column3 = st.columns(3)

#Test - all qubits set to 0, later give the user choice to choose initial qubit of choice.
#Leftmost column - Gate selection, display and explanation. 
with column1:
    st.header("Take your pick!")
    # Build a new circuit
    qc = QuantumCircuit(1)
    if initial_choice == "|1⟩":
        qc.x(0)  #Flipping the qubit if the user chooses the initial state to be |1⟩
    status = qc.draw(output="mpl")

    # Gate selection
    gate = st.selectbox("Choose a gate to apply:", ["H", "X", "Y", "Z", "S", "T"], help="Select a gate to apply to the qubit. Each gate rotates the qubit in a unique way.")
    apply_button = st.button("Apply Gate")

    # Apply the selected gate
    if apply_button:
        if gate == "H":
            h_gate(qc, 0)
            status = qc.draw(output="mpl", scale=0.75)
            st.pyplot(status)
            with st.expander("ℹ️ H Gate"):
                st.write('''
                    The **Hadamard (H) gate** is one of the most important quantum gates.  
                    It transforms a classical state (|0⟩ or |1⟩) into a superposition — a state where the qubit has a probability of being both 0 and 1 until measured.

                    - On |0⟩: It becomes (|0⟩ + |1⟩)/√2  
                    - On |1⟩: It becomes (|0⟩ - |1⟩)/√2  
                    
                    This is also reflected as a rotation that brings the qubit from the pole of the Bloch Sphere onto its equator.
                ''')
            
        elif gate == "X":
            not_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)  
            with st.expander("ℹ️ X Gate"):
                st.write('''
                    The X gate, also called the NOT or bit-flip gate, swaps |0⟩ and |1⟩.

                    - If the qubit is in |0⟩, it flips to |1⟩.  
                    - If it's in |1⟩, it flips to |0⟩.  
                    
                    On the Bloch Sphere, this is a 180° rotation around the X-axis, moving the qubit between the north and south poles.
                ''')

        elif gate == "Y":
            y_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)
            with st.expander("ℹ️ Y Gate"):
                st.write('''
                    The Y gate is another rotation gate like X and Z. It performs a 180° rotation around the Y-axis.

                    - On |0⟩, it takes the qubit to i|1⟩.  
                    - On |1⟩, it becomes –i|0⟩.  

                    Although it flips between |0⟩ and |1⟩ like X, it adds a complex phase (±i), which becomes important when building quantum algorithms.

                    You’ll see this rotation clearly if the qubit starts in a superposition.
                ''')

        elif gate == "Z":
            z_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)
            with st.expander("ℹ️ Z Gate"):
                st.write('''
                    The Z gate, or phase-flip gate, leaves |0⟩ unchanged and flips the sign of |1⟩.

                    - It maps |0⟩ → |0⟩  
                    - It maps |1⟩ → –|1⟩  

                    On the Bloch Sphere, this means a 180° rotation around the Z-axis.  
                    If your qubit starts at |0⟩ or |1⟩ (the poles), you won’t see a change, since it’s just a phase shift. But this has big implications in interference and entanglement!
                ''')

        elif gate == "S":
            s_gate(qc, 0)
            status = qc.draw(output="mpl")
            st.pyplot(status)
            with st.expander("ℹ️ S Gate"):
                st.write('''
                    The S gate is also called the phase gate.  

                    - It adds a π/2 (90°) phase to the |1⟩ component of the qubit.  
                    - |0⟩ remains unchanged.  
                    - |1⟩ becomes i|1⟩ (where *i* is the imaginary unit).  

                    Like Z, it rotates the qubit around the Z-axis, so it won’t visibly affect the Bloch Sphere unless the qubit is in a superposition state.
                ''')

        elif gate == "T":
            t_gate(qc, 0)
            with st.expander("ℹ️ T Gate"):
                st.write('''
                    The T gate is a π/4 (45°) phase gate.  

                    - It keeps |0⟩ unchanged.  
                    - It transforms |1⟩ into e^{iπ/4}|1⟩, a complex rotation.  

                    This gate is useful for fine-tuning quantum states and creating more subtle phase differences.  
                    It’s essential in building universal quantum circuits, even though it looks simple.

                    Like the S gate, its effect is clearer when applied after a Hadamard or in superposition.
                ''')

#Centre Column - A glimpse of the actual algebra going on in the background.
with column2:
    st.header("The Math Behind It")
    st.subheader(f"Initial State: {initial_choice}")
    display_initial_state(initial_choice)

    if apply_button:
        if gate == "H":
            st.subheader("H Gate Matrix")
            final_state = get_h_gate_matrix() @ get_initial_state(initial_choice)
            latex_final = array_to_latex(final_state)
            display_h_gate()
            st.latex(f"{gate} \\cdot {initial_choice} = " + latex_final)

        elif gate == "X":
            st.subheader("X Gate Matrix")
            final_state = get_x_gate_matrix() @ get_initial_state(initial_choice)
            latex_final = array_to_latex(final_state)
            display_x_gate()
            st.latex(f"{gate} \\cdot {initial_choice} = " + latex_final)

        elif gate == "Y":
            st.subheader("Y Gate Matrix")
            final_state = get_y_gate_matrix() @ get_initial_state(initial_choice)
            latex_final = array_to_latex(final_state)
            display_y_gate()
            st.latex(f"{gate} \\cdot {initial_choice} = " + latex_final)

        elif gate == "Z":
            st.subheader("Z Gate Matrix")
            final_state = get_z_gate_matrix() @ get_initial_state(initial_choice)
            latex_final = array_to_latex(final_state)
            display_z_gate()
            st.latex(f"{gate} \\cdot {initial_choice} = " + latex_final)

        elif gate == "S":
            st.subheader("S Gate Matrix")
            final_state = get_s_gate_matrix() @ get_initial_state(initial_choice)
            latex_final = array_to_latex(final_state)
            display_s_gate()
            st.latex(f"{gate} \\cdot {initial_choice} = " + latex_final)

        elif gate == "T":
            st.subheader("T Gate Matrix")
            final_state = get_t_gate_matrix() @ get_initial_state(initial_choice)
            latex_final = array_to_latex(final_state)
            display_t_gate()
            st.latex(f"{gate} \\cdot {initial_choice} = " + latex_final)

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
    try:
        fig = plot_bloch_multivector(state.data)
        fig.set_size_inches(4, 4)
        st.pyplot(fig)
    except Exception as e:
        st.error("There has been an issue with the Bloch Sphere rendering.")
        st.exception(e)
