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
