
# SFAT - Extended Python Model with Theory, Normalization, and Time Dynamics (v2.0)
# Author: Manuel Zago (Independent Researcher)
# Date: July 25, 2025

from math import log, cos, pi, sqrt
import numpy as np
import pandas as pd

# === FUNDAMENTAL CONSTANTS ===
PHI = (1 + sqrt(5)) / 2          # Golden Ratio φ (dimensionless)
OMEGA = 2 * pi                   # Oscillation frequency (rad)
KAPPA = 0.1                      # Log-periodic coupling (unit: GeV^4 or abstract)
LAMBDA_LIFE = 0.05              # Life-field coupling (unitless, scalable)
x0 = 1.0                         # Origin point (Big Bang reference) [unit: arbitrary, normalized]
t0 = 1.0                         # Reference time unit [unit: seconds, normalized]

# === CORE FORMULAS ===
def sigma(x):
    """Fractal scale field σ(x) = ln(x/x0) / ln(φ)"""
    return log(x / x0) / log(PHI)

def V_log_periodic(sigma_val):
    """Log-periodic potential V(σ) = κ cos(ωσ)"""
    return KAPPA * cos(OMEGA * sigma_val)

def rho_bio_raw(x, center=2.0, width=0.3):
    """Unnormalized biological density (Gaussian)"""
    return np.exp(-((x - center)**2) / (2 * width**2))

# Compute normalization constant for rho_bio
x_range = np.linspace(0.5, 3.5, 200)
rho_vals = np.array([rho_bio_raw(x) for x in x_range])
rho_max = np.max(rho_vals)

def rho_bio(x):
    """Normalized biological density"""
    return rho_bio_raw(x) / rho_max

def L_total(x):
    """Total Lagrangian with life-coupling"""
    s = sigma(x)
    V_sigma = V_log_periodic(s)
    life_term = rho_bio(x) * LAMBDA_LIFE
    return V_sigma + life_term

def sigma_time(t, n=1):
    """Time evolution of σ: σ(t) = ln(t/t0) / ln(φ)"""
    return log(t / t0) / log(PHI)

# === THEORY PILLARS - 13 FOUNDATIONS ===
SFAT_PILLARS = [
    "1. Origin: Point Zero (Big Bang) as universal reference x0.",
    "2. Perfect Sphere: All objects originate as ideal spheres.",
    "3. Golden Ratio φ: Discrete scale evolution x → x·φⁿ.",
    "4. Pi π: Topological constraint for angular closure.",
    "5. Fractal Field σ(x): Measures depth from x0 via log(φ).",
    "6. Environmental Deformers: Fields like gravity, radiation.",
    "7. Life: Alters σ(x), introduces memory & organization.",
    "8. Observation: Modifies the system actively (contextuality).",
    "9. Time: Emergent quantity, t ∝ φⁿ.",
    "10. Log-Periodic Law: Universal correction formula.",
    "11. Fractal Hierarchy: Phenomena appear at φⁿ nodes.",
    "12. Interdisciplinary Integration: Physics, bio, math, info.",
    "13. Expansion Factor a(t): Redshift correction with φ."
]

# === SIMULATED SPACE-TIME DYNAMICS ===
x_values = np.linspace(0.5, 3.5, 200)
t_values = np.linspace(1, 10, 200)

results = {
    'x [a.u.]': x_values,
    'σ(x)': [sigma(x) for x in x_values],
    'V_log [a.u.]': [V_log_periodic(sigma(x)) for x in x_values],
    'ρ_bio(x) [norm]': [rho_bio(x) for x in x_values],
    'life_term [a.u.]': [rho_bio(x) * LAMBDA_LIFE for x in x_values],
    'L_total [a.u.]': [L_total(x) for x in x_values]
}

time_results = {
    't [s]': t_values,
    'σ(t)': [sigma_time(t) for t in t_values]
}

df_space = pd.DataFrame(results)
df_time = pd.DataFrame(time_results)

# === DISPLAY THEORY PILLARS IN CONSOLE ===
print("=== SFAT: 13 Foundational Pillars ===")
for line in SFAT_PILLARS:
    print(line)

# === OUTPUT TABLES ===
import ace_tools as tools
tools.display_dataframe_to_user(name="SFAT - Spatial Model with Life Coupling", dataframe=df_space)
tools.display_dataframe_to_user(name="SFAT - Temporal Evolution of σ(t)", dataframe=df_time)
