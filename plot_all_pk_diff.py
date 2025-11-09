#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
En-tête universel pour scripts de visualisation CLASS
-----------------------------------------------------
- Choisit automatiquement le backend Matplotlib :
    • Qt5Agg si environnement graphique (DISPLAY présent)
    • Agg sinon (mode batch / SSH / WSL)
- Configure le style d'affichage et les figures
- Crée le dossier 'output' si inexistant
- Affiche les infos système et backend choisi
"""

import os
import sys
import platform
import matplotlib

# === Détection du mode graphique ou non ===
if os.environ.get("DISPLAY"):
    backend = "Qt5Agg"
else:
    backend = "Agg"

matplotlib.use(backend)

# === Imports standards ===
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# === Préparation environnement ===
OUTDIR = "output"
os.makedirs(OUTDIR, exist_ok=True)

print(f"--- Script lancé le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
print(f"Système     : {platform.system()} {platform.release()}")
print(f"Python      : {sys.version.split()[0]}")
print(f"Matplotlib  : {matplotlib.__version__}")
print(f"Backend     : {matplotlib.get_backend()}")
print(f"Dossier out : {os.path.abspath(OUTDIR)}")
print("---------------------------------------------------------------")

# === Style Matplotlib ===
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "figure.figsize": (9, 6),
    "font.size": 12,
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "legend.fontsize": 11,
    "lines.linewidth": 2,
    "grid.alpha": 0.3
})

# === Fonction utilitaire ===
def save_fig(name):
    """Sauvegarde standardisée dans le dossier output"""
    path = os.path.join(OUTDIR, name)
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    print(f"✅ Figure enregistrée : {path}")

if os.environ.get("DISPLAY"):
    backend = "TkAgg"
else:
    backend = "Agg"


# Charge les spectres
lcdm = np.loadtxt("output/mon_modele_LCDM00_pk.dat")
rgh  = np.loadtxt("output/mon_modele_RGH00_pk.dat")

# Colonnes CLASS : k [h/Mpc], P(k) [Mpc³/h³]
k_LCDM, P_LCDM = lcdm[:,0], lcdm[:,1]
k_RGH,  P_RGH  = rgh[:,0],  rgh[:,1]

# Interpolation RGH sur la grille de LCDM
P_RGH_interp = np.interp(k_LCDM, k_RGH, P_RGH)

# Différence relative
delta = (P_RGH_interp - P_LCDM) / P_LCDM

# --- Figure ---
fig, ax = plt.subplots(2, 1, figsize=(9,8), sharex=True,
                       gridspec_kw={"height_ratios":[3,1]})

# --- Spectres ---
ax[0].loglog(k_LCDM, P_LCDM, 'b--', lw=2, label='ΛCDM')
ax[0].loglog(k_LCDM, P_RGH_interp, 'orange', lw=2, label='RGH (interp)')
ax[0].set_ylabel(r'$P(k)\ [\mathrm{Mpc}^3/h^3]$', fontsize=12)
ax[0].legend(fontsize=10)
ax[0].grid(True, which='both', alpha=0.3)
ax[0].set_title('Spectre de puissance P(k) et écart relatif RGH vs ΛCDM')

# --- Différence relative ---
ax[1].semilogx(k_LCDM, delta*100, 'k-', lw=1.5)
ax[1].axhline(0, color='gray', lw=0.8)
ax[1].set_xlabel(r'$k\ [h/\mathrm{Mpc}]$', fontsize=12)
ax[1].set_ylabel(r'Δ[%]', fontsize=12)
ax[1].grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.savefig("P_k_diff.png", dpi=200)
plt.show()
