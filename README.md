## ⚛️ Quantum Well Solver

A numerical simulation project for solving a 1-D quantum well systems using Python.

## 📊 Example Output

![/imgaes/quantum_well_wavefuntions.png](/images/quantum_well_wavefuntions.png)
![quantum_well_probabilities.png](/images/quantum_well_probabilities.png)



## 🧠 Overview

This project solves the time-independent Schrödinger equation for a particle in an infinte potential well and computes :

 -  Energy eigenvalues
 -  Eigenfunctions (wavefunctions)
 -  Probability distributions

## 🔬 Methods
 -  Finite difference for discretizing differential equations
 -  Matrix eigenvalue decomposition
 -  Numerical linear algebra using NumPy


## 📊 Features
 -  Solve bound states in quantum wells
 -  Visualize wavefunctions
 -  Plot energy levels
 -  Explore how potential shapes affect solutions


## 🛠️ Tech Stack
 -  Python
 -  NumPy
 -  Matplotlib

## ⭐ Highlights

This project demonstrates:
 - Strong foundation in quantum mechanics and mathematical physics
 - Ability to translate theory into working numerical simulations
 - Experience with scientific computing and numerical methods
 - Pedagogical illustration for quantum physics education
 - The code is intentionally **simple and self‑contained**, and can be run on a local machine without any external API or internet connection.

---

## 🧰 Installation

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

## 🔍 How to Run

Execute the main script
```bash
python solve_1d_quantum_well.py

```
This will:
- Print the first `n_basis` energy levels(by default 5).

- Plot and save two figures:
  -  `quantum_well_wavefunctions.png`: shifted eigenfunctions.
  -  `quantum_well_probabilities.png`: probability densities.
 


## 🏗️ Project Structure

```bash
quantum-well-solver/
├── solve_1d_quantum_well.py      
├── README.md                    
├── images/                       
│   ├── quantum_well_wavefunctions.png
│   └── quantum_well_probabilities.png
└── requirements.txt

```            


## 🚀 Mathematics (Brief)

For a 1D infinite square well of length L with m = 1, ħ = 1:

- Eigenfunctions:
  ψ_n(x) = sqrt(2/L) * sin(n*pi*x/L),   for x in [0, L]

- Eigenenergies:
  E_n = (n^2 * pi^2) / (2*L^2)

## 👩‍💻 Author
Shi-Ning Caren Yang

## 🌐 License
The code is released under the MIT License (or the license you choose).  
It is intended for educational / demonstration purposes, not for production‑level scientific computing.

## 📚 Acknowledgements
This example is inspired by standard quantum mechanics textbooks and numerical physics resources.  
See, for example, pedagogical notes on solving the 1-D Schrödinger equation numerically with Python.


