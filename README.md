
# SFAT - Golden Ratio Fractal Field Theory

This repository contains the Python code to simulate and validate the **Fractal Golden Field Theory (SFAT)**, a model based on discrete scale invariance derived from the golden ratio (φ) and log-periodic corrections.

## Contents

- Computation of the fractal field σ(x)
- Log-periodic potential V(σ)
- Oscillating beta function β(g)
- SFAT cosmological predictions (redshift, BAO, CMB)
- Graphs and outputs for comparison with ΛCDM

## Requirements

```bash
pip install numpy matplotlib
```

## Example Usage

```python
from sfat import calculate_sigma, log_periodic_potential, beta_function, cosmological_predictions

sigma = calculate_sigma(2.5)
potential = log_periodic_potential(sigma)
beta = beta_function(0.1)
prediction = cosmological_predictions(0.7)

print(f"σ(x) = {sigma:.4f}")
print(f"V(σ) = {potential:.4f}")
print(f"β(g) = {beta:.4f}")
print(f"SFAT vs ΛCDM = {prediction}")
```

## License

Distributed under the MIT License.

## Reference

The model is described in detail in the scientific paper:  
*Fractal Golden Field Theory (SFAT): A Unified Formulation of Physics via Fractal Scaling*,  
Manuel Zago, 2025.
