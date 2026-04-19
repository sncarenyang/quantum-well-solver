# solve_1d_quantum_well.py
# 1D infinite square well (particle in a box)
# Numerically solve the time‑independent Schrödinger equation
# and plot the first few eigenstates.

import numpy as np
import matplotlib.pyplot as plt

def solve_1d_infinite_well(x_min=0, x_max=1, N=1000, n_basis=5):
    """
    Numerically compute eigenstates of 1D infinite square well
    on [x_min, x_max] using analytic formula (no heavy numerics).

    Parameters
    ----------
    x_min, x_max : float
        spatial domain
    N : int
        number of grid points
    n_basis : int
        number of eigenstates to compute (n=1,2,...,n_basis)

    Returns
    -------
    x, psi_list, energies
        x: grid points
        psi_list: list of normalized eigenfunctions
        energies: list of eigenenergies (E_n)
    """

    x = np.linspace(x_min, x_max, N)
    dx = x[1] - x[0]

    # mass = 1, hbar = 1, L = 1 (so E_n = n^2 * pi^2 / 2)
    L = x_max - x_min
    m = 1.0
    hbar = 1.0

    psi_list = []
    energies = []

    for n in range(1, n_basis + 1):
        k = n * np.pi / L
        psi = np.sqrt(2 / L) * np.sin(k * (x - x_min))

        # normalization check
        norm = np.sqrt(np.sum(psi**2) * dx)
        psi = psi / norm

        # energy (E_n = n^2 * pi^2 / (2 m L^2))
        E = n**2 * np.pi**2 / (2 * m * L**2)

        psi_list.append(psi)
        energies.append(E)

    return x, psi_list, energies


def main():
    x_min, x_max = 0.0, 1.0
    x, psi_list, energies = solve_1d_infinite_well(
        x_min=x_min,
        x_max=x_max,
        N=1000,
        n_basis=5
    )

    # 打印前五個能階
    print("Energy levels (n=1,2,3,4,5):")
    for n, E in enumerate(energies, start=1):
        print(f"n={n}: E = {E:.4f}")

    # 畫圖：波函數
    plt.figure(figsize=(9, 6))

    for n, psi in enumerate(psi_list, start=1):
        offset = (n - 1) * 1.8
        psi_shifted = psi + offset
        plt.plot(x, psi_shifted, label=f"n={n}", lw=2)

    plt.axhline(y=0, color="k", linestyle="--", alpha=0.5)
    plt.xlabel("Position $x$")
    plt.ylabel("Wave function $\\psi(x)$ (shifted)")
    plt.title("1D Infinite Square Well — First 5 Eigenstates")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig("quantum_well_wavefunctions.png", dpi=150, bbox_inches="tight")
    plt.show()

    # 畫圖：機率密度
    plt.figure(figsize=(7, 5))
    for n, psi in enumerate(psi_list, start=1):
        prob = psi**2
        plt.plot(x, prob, label=f"n={n}", lw=2)

    plt.xlabel("Position $x$")
    plt.ylabel("Probability density $|\\psi(x)|^2$")
    plt.title("1D Infinite Square Well — Probability Densities")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig("quantum_well_probabilities.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
