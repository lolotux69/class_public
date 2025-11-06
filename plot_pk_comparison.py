# plot_pk_comparison.py
import matplotlib.pyplot as plt
import numpy as np

# RGH
rgh = np.loadtxt("output/mon_modele_RGH00_pk.dat")
k_rgh = rgh[:,0]
P_rgh = rgh[:,1]

# ΛCDM
lcdm = np.loadtxt("output/explanatory00_pk.dat")
k_lcdm = lcdm[:,0]
P_lcdm = lcdm[:,1]

plt.figure(figsize=(10,7))
plt.loglog(k_rgh, P_rgh, 'b-', linewidth=2, label='RGH (α_W = 0.1)')
plt.loglog(k_lcdm, P_lcdm, 'r--', linewidth=2, label='ΛCDM')
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('P(k) [Mpc³/h³]', fontsize=12)
plt.title('P(k) : RGH vs ΛCDM', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('P_k_RGH_vs_LCDM.png', dpi=200)
print("Image générée : P_k_RGH_vs_LCDM.png")

