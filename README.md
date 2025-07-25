# SFAT - Golden Ratio Fractal Field Theory

Questo repository contiene il codice Python per simulare e verificare la **Teoria di Campo Frattale Aurea (SFAT)**, basata su simmetrie di scala discreta fondate sulla sezione aurea (φ) e correzioni log-periodiche.

## Contenuti

- Calcolo del campo frattale σ(x)
- Potenziale log-periodico V(σ)
- Funzione beta oscillante β(g)
- Predizioni cosmologiche SFAT (redshift, BAO, CMB)
- Grafici e output per il confronto con ΛCDM

## Requisiti

```bash
pip install numpy matplotlib
```

## Esempio di utilizzo

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

## Licenza

Distribuito sotto licenza MIT.

## Riferimenti

Il modello è descritto in dettaglio nel paper:
*Teoria di Campo Frattale Aurea (SFAT): Una Formulazione Unificata della Fisica attraverso la Scala Frattale*, Manuel Zago, 2025.
