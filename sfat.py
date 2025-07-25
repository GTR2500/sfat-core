"""
Modulo SFAT: Teoria di Campo Frattale Aurea
Autore: Manuel Zago
"""

import numpy as np

# Costanti fondamentali
PHI = (1 + np.sqrt(5)) / 2  # Sezione aurea
M_P = 1.22e19  # Massa di Planck in GeV

# Campo frattale sigma(x)
def calculate_sigma(x, x0=1.0):
    return np.log(x / x0) / np.log(PHI)

# Potenziale log-periodico V(sigma)
def log_periodic_potential(sigma, kappa=0.1, omega=2 * np.pi):
    return kappa * np.cos(omega * sigma)

# Funzione beta con oscillazioni
def beta_function(g, amplitude=0.05):
    if g <= 0:
        return np.nan  # evita log di numeri <= 0
    return -g + g**3 + amplitude * np.sin(2 * np.pi * np.log(g) / np.log(PHI))

# Predizioni cosmologiche SFAT (vs Lambda-CDM)
def cosmological_predictions(z):
    sigma_z = calculate_sigma(1 + z)
    correction = 1 + 0.02 * np.cos(2 * np.pi * sigma_z)
    sfat_value = 0.698 * correction
    lambda_cdm_value = 0.698
    deviation_percent = (sfat_value - lambda_cdm_value) / lambda_cdm_value * 100
    return {
        "sfat": sfat_value,
        "lambdaCDM": lambda_cdm_value,
        "deviation_percent": deviation_percent
    }

# Esecuzione di esempio
if __name__ == "__main__":
    z = 0.7
    result = cosmological_predictions(z)
    print(f"Predizione per z = {z}")
    print(f"SFAT: {result['sfat']:.6f}, ΛCDM: {result['lambdaCDM']:.6f}, Δ%: {result['deviation_percent']:.2f}%")
