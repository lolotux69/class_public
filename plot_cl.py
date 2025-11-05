# plot_cl.py
# Spectres CMB de ton modèle RGH vs ΛCDM

import matplotlib.pyplot as plt
import numpy as np

# === 1. Charge ton modèle RGH ===
rgh = np.loadtxt("output/mon_modele_RGH00_cl_lensed.dat")
l_rgh = rgh[:, 0]
TT_rgh = rgh[:, 1] * l_rgh * (l_rgh + 1) / (2 * np.pi)  # [μK²]
EE_rgh = rgh[:, 2] * l_rgh * (l_rgh + 1) / (2 * np.pi)

# === 2. Charge ΛCDM (explanatory00) ===
lcdm = np.loadtxt("output/explanatory00_cl_lensed.dat")
l_lcdm = lcdm[:, 0]
TT_lcdm = lcdm[:, 1] * l_lcdm * (l_lcdm + 1) / (2 * np.pi)
EE_lcdm = lcdm[:, 2] * l_lcdm * (l_lcdm + 1) / (2 * np.pi)

# === 3. Plot TT ===
plt.figure(figsize=(10, 6))
plt.plot(l_rgh[2:], TT_rgh[2:], 'b-', label='RGH (α_W = 0.1)', linewidth=2)
plt.plot(l_lcdm[2:], TT_lcdm[2:], 'r--', label='ΛCDM', linewidth=2)
plt.xlabel('Multipôle ℓ', fontsize=12)
plt.ylabel('ℓ(ℓ+1)C_ℓᵀᵀ / 2π  [μK²]', fontsize=12)
plt.title('Spectre CMB TT - RGH vs ΛCDM', fontsize=14)
plt.xlim(2, 2500)
plt.ylim(0, 6000)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('CMB_TT_RGH.png', dpi=200)
print("TT sauvé : CMB_TT_RGH.png")

# === 4. Plot EE ===
plt.figure(figsize=(10, 6))
plt.plot(l_rgh[2:], EE_rgh[2:], 'b-', label='RGH (α_W = 0.1)', linewidth=2)
plt.plot(l_lcdm[2:], EE_lcdm[2:], 'r--', label='ΛCDM', linewidth=2)
plt.xlabel('Multipôle ℓ', fontsize=12)
plt.ylabel('ℓ(ℓ+1)C_ℓᴱᴱ / 2π  [μK²]', fontsize=12)
plt.title('Spectre CMB EE - RGH vs ΛCDM', fontsize=14)
plt.xlim(2, 2000)
plt.ylim(0, 50)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('CMB_EE_RGH.png', dpi=200)
print("EE sauvé : CMB_EE_RGH.png")

