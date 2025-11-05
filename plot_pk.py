# plot_pk.py
import matplotlib.pyplot as plt
import numpy as np

# Charge ton spectre
data = np.loadtxt("output/mon_modele_RGH00_pk.dat")
k = data[:,0]
P = data[:,1]

# Plot
plt.figure(figsize=(9,6))
plt.loglog(k, P, 'b-', linewidth=2, label='RGH (α_W = 0.1)')
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('P(k) [Mpc³/h³]', fontsize=12)
plt.title('Spectre de puissance - Modèle RGH', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('P_k_RGH.png', dpi=200)
print("Image sauvegardée : P_k_RGH.png")

# Ajoute dans plot_pk.py
lcdm = np.loadtxt("output/explanatory00_pk.dat")
plt.loglog(lcdm[:,0], lcdm[:,1], 'r--', label='ΛCDM')

