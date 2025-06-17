# Quantum Gates Playground

An interactive Streamlit-based simulator that lets you visualize quantum gate operations on a single qubit — and learn about quantum computing concepts along the way.

![Bloch Sphere Screenshot](link-to-screenshot-if-you-have-one)

---

## What This Project Is

This is not just a simulator — it's a **hands-on learning tool** for beginners in quantum computing. Choose a qubit state, apply quantum gates like Hadamard, Pauli-X, or phase gates, and watch how your qubit transforms on the Bloch sphere.

> Curious why applying Hadamard twice gives you back your original state? You'll find out here.

---

## Features

- ✅ Choose an initial qubit state
- ✅ Apply gates like H, X, Z, S, T, etc.
- ✅ Visualize qubit state changes on a Bloch sphere
- ✅ Get educational insights into what each gate does
- ✅ Try suggested gate combinations and understand the outcomes

---

## Tech Stack

- [Streamlit](https://streamlit.io/) — UI and interaction
- [Qiskit](https://qiskit.org/) — Quantum simulation and Bloch vector math
- [Matplotlib / Plotly (optional)] — For Bloch sphere rendering

---

## How to Run the App

### 1. Clone the repository

git clone https://github.com/your-username/quantum-gates-playground.git
cd quantum-gates-playground

### 2. Install dependencies

pip install -r requirements.txt

You’ll need:
qiskit
streamlit
matplotlib or plotly (choose one or both)

### 3. Run the Streamlit app
streamlit run app.py

## Learn as You Explore
This app will gently guide you to learn:

- What each gate does geometrically
- How Bloch sphere rotations relate to gates
- Commutativity, reversibility, and fun quirks in quantum logic


## Educational Goals
This tool was created to:

- Help students and enthusiasts develop geometric intuition
- Be a lightweight alternative to full Qiskit notebooks
- Make exploring quantum concepts fun and interactive


## Contributing
PRs, feedback, and feature ideas are welcome!
Please open an issue if you'd like to collaborate or improve the educational material.

## License
MIT License

## Author
LinkedIn: https://www.linkedin.com/in/safura-kasu-544b50281/ Email: safurakasu@gmail.com
