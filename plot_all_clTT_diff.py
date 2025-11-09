#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

lcdm = np.loadtxt("output/mon_modele_LCDM00_cl_lensed.dat")
rgh  = np.loadtxt("output/mon_modele_RGH00_cl_lensed.dat")

# Récupère les colonnes ℓ et Dℓ
ell_LCDM, Dl_LCDM = lcdm[:,0], lcdm[:,1]
ell_RGH,  Dl_RGH  = rgh[:,0],  rgh[:,1]

# Interpole RGH sur la grille de LCDM
Dl_RGH_interp = np.interp(ell_LCDM, ell_RGH, Dl_RGH)

# Différence relative
delta = (Dl_RGH_interp - Dl_LCDM) / Dl_LCDM

fig, ax = plt.subplots(2, 1, figsize=(9,8), sharex=True,
                       gridspec_kw={"height_ratios":[3,1]})

# --- Spectres ---
ax[0].semilogx(ell_LCDM, Dl_LCDM, 'b--', lw=2, label='ΛCDM')
ax[0].semilogx(ell_LCDM, Dl_RGH_interp, 'orange', lw=2, label='RGH (interp)')
ax[0].set_ylabel(r'$D_\ell^{TT}\ [\mu K^2]$', fontsize=12)
ax[0].legend(fontsize=10)
ax[0].grid(True, alpha=0.3)
ax[0].set_title('Spectre CMB TT et écart relatif RGH vs ΛCDM')

# --- Résidu relatif ---
ax[1].semilogx(ell_LCDM, delta*100, 'k-', lw=1.5)
ax[1].axhline(0, color='gray', lw=0.8)
ax[1].set_xlabel(r'$\ell$', fontsize=12)
ax[1].set_ylabel(r'Δ[%]', fontsize=12)
ax[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("CMB_TT_diff.png", dpi=200)
plt.show()
