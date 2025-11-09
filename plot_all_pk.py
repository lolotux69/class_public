#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# Dossier contenant les sorties CLASS
output_dir = "output"

# Recherche tous les fichiers de spectre P(k)
pk_files = sorted(glob.glob(os.path.join(output_dir, "*_pk.dat")))

if not pk_files:
    print(f"Aucun fichier *_pk.dat trouvé dans {output_dir}/")
    exit(1)

plt.figure(figsize=(9, 6))

# Boucle sur tous les fichiers trouvés
for f in pk_files:
    try:
        data = np.loadtxt(f)
        k, P = data[:, 0], data[:, 1]
        label = os.path.basename(f).replace("_pk.dat", "")
        plt.loglog(k, P, linewidth=2, label=label)
    except Exception as e:
        print(f"⚠️ Erreur lecture {f}: {e}")

plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('P(k) [Mpc³/h³]', fontsize=12)
plt.title('Spectres de puissance - Comparaison de modèles', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()

# Sauvegarde + affichage
plt.savefig('P_k_all.png', dpi=200)
plt.show()
print(f"✅ Image sauvegardée : P_k_all.png ({len(pk_files)} modèles tracés)")
