# plot_pk-02.py
import matplotlib.pyplot as plt
import numpy as np

# === RGH ===
rgh = np.loadtxt("output/mon_modele_RGH00_pk.dat")
k_rgh = rgh[:, 0]
P_rgh = rgh[:, 1]

# === LCDM ===
lcdm = np.loadtxt("output/explanatory00_pk.dat")
k_lcdm = lcdm[:, 0]
P_lcdm = lcdm[:, 1]

# === Plot ===
plt.figure(figsize=(9, 6))
plt.loglog(k_lcdm, P_lcdm, 'r--', linewidth=2, label='ΛCDM')
plt.loglog(k_rgh, P_rgh, 'b-', linewidth=2, label='RGH (α_W = 0.1)')

plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('P(k) [Mpc³/h³]', fontsize=12)
plt.title('Spectre de puissance - Comparaison RGH vs ΛCDM', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('P_k_RGH.png', dpi=200)
plt.show()
print("✅ Image sauvegardée : P_k_RGH.png")
