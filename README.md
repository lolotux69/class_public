# CLASS + RGH Model

**Modèle cosmologique RGH (Relativité Générale Holographique)**  
Ajout d'une nouvelle composante d'énergie :  
**`ρ_θ = α_W × H₀² / a²`**  
→ Active **uniquement pour `z < 99`**

---

## Caractéristiques

| Propriété | Valeur |
|---------|--------|
| `α_W` | `0.1` |
| Activation | `z < 99` (`a > 0.01`) |
| Effet sur CMB (TT, EE) | **Aucun** (compatible Planck) |
| Effet sur P(k) | **Pic plus haut + décalé vers k ≈ 0.03 h/Mpc** |
| Croissance des structures | **Augmentée à petite échelle** |

---

## Fichiers inclus

- `mon_modele_RGH.ini` → Paramètres du modèle
- `source/background.c` → Implémentation de `ρ_θ`
- `source/input.c` → Lecture de `α_W`
- `include/constants.h` → Constantes physiques
- `plot_pk.py` → Plot P(k) vs ΛCDM
- `plot_cl.py` → Plot C_ℓ (TT, EE) vs ΛCDM

---

## Installation

```bash
make clean && make

