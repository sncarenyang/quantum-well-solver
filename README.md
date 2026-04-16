# quantum-well-solver
# 1D Infinite Quantum Well Solver

A simple numerical solver for the 1D infinite square well ("particle in a box") problem in quantum mechanics.  
It computes the first few eigenstates and eigenenergies, and plots the wave functions and probability densities using Python + NumPy + Matplotlib.

---

## 1. Overview

This repository provides a pedagogical implementation of:

- The time‑independent Schrödinger equation for a 1D particle in an infinite square well.  
- Analytic eigenfunctions and eigenenergies for the first few bound states.  
- Visualizations of wave functions and probability densities along the box.

The code is intentionally **simple and self‑contained**, and can be run on a local machine without any external API or internet connection.

---

## 2. Installation

Create a virtual environment and install the dependencies:

```bash
git clone https://github.com/sncarenyang/quantum-well-solver.git
cd quantum-well-solver

python -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate     # Windows

pip install -r requirements.txt
```
---

## 3. How to Run

Execute the main script
```bash
python solve_1d_quantum_well.py

```
This will:
- Print the first `n_basis` energy levels(by default 5).

- Plot and save two figures:
  -  `quantum_well_wavefunctions.png`: shifted eigenfunctions.
  -  `quantum_well_probabilities.png`: probability densities.

## 4. Project Structure

```bash
quantum-well-solver/
├── solve_1d_quantum_well.py      
├── README.md                    
├── images/                       
│   ├── quantum_well_wavefunctions.png
│   └── quantum_well_probabilities.png
└── requirements.txt

```            


## 5. Mathematics (Brief)

For a 1D infinite square well of length L with m = 1, ħ = 1:

- Eigenfunctions:
  ψ_n(x) = sqrt(2/L) * sin(n*pi*x/L),   for x in [0, L]

- Eigenenergies:
  E_n = (n^2 * pi^2) / (2*L^2)

## 6. License
The code is released under the MIT License (or the license you choose).  
It is intended for educational / demonstration purposes, not for production‑level scientific computing.

## 7. Acknowledgements
This example is inspired by standard quantum mechanics textbooks and numerical physics resources.  
See, for example, pedagogical notes on solving the 1-D Schrödinger equation numerically with Python.


