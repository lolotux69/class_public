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



## Lancer le modèle
bash./class mon_modele_RGH.ini

## → Génère :

output/mon_modele_RGH00_pk.dat
output/mon_modele_RGH00_cl_lensed.dat


## Plots
bash# Dans un venv avec matplotlib
python3 -m venv class_env
source class_env/bin/activate
pip install matplotlib numpy
python3 plot_pk.py
python3 plot_cl.py
→ Génère :

P_k_RGH.png
CMB_TT_RGH.png
CMB_EE_RGH.png


Auteur
Laurent (lolotux69)
Novembre 2025


Modèle testable avec SDSS, DESI, Euclid
Prêt pour publication

