#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import glob, os

def load_TT_Dl(path):
    """Charge Dl = l(l+1)C_l/2pi [µK²], en détectant si C_l ou Dl est donné"""
    data = np.loadtxt(path)
    ell = data[:,0]
    col = data[:,1]
    vmax = np.max(col)
    if vmax > 1e2:
        Dl = col
    else:
        Tcmb_muK = 2.7255e6
        Dl = ell*(ell+1)/(2*np.pi) * col * (Tcmb_muK**2)
    return ell, Dl

# Cherche tous les fichiers *_cl_lensed.dat
files = sorted(glob.glob(os.path.join("output", "*_cl_lensed.dat")))
if not files:
    print("⚠️ Aucun fichier *_cl_lensed.dat trouvé dans output/")
    raise SystemExit

plt.figure(figsize=(9,6))

# Pour des couleurs/traits alternés
styles = [
    {"color": "royalblue", "ls": "--", "lw": 2},  # ΛCDM
    {"color": "orange", "ls": "-", "lw": 2},      # RGH
    {"color": "green", "ls": "-.", "lw": 2},      # Optionnel : RGH-02
    {"color": "red", "ls": ":", "lw": 2},         # Optionnel
]

for i, f in enumerate(files):
    ell, Dl = load_TT_Dl(f)
    label = os.path.basename(f).replace("_cl_lensed.dat", "")
    st = styles[i % len(styles)]
    plt.semilogx(ell, Dl, label=label, **st)

plt.xlabel(r'$\ell$', fontsize=12)
plt.ylabel(r'$D_\ell^{TT} = \ell(\ell+1)C_\ell^{TT}/2\pi\ [\mu{\rm K}^2]$', fontsize=12)
plt.title('Spectre CMB TT - Comparaison de modèles', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("CMB_TT_all.png", dpi=200)
plt.show()
print("✅ Image écrite : CMB_TT_all.png")
