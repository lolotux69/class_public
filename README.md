<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/73/Relativity_icon.svg" alt="RGH Logo" width="100"/>
</p>

<h1 align="center">Relativité Générale Hypercomplexe (RGH)</h1>
<h3 align="center">Extension quaternionique du code cosmologique CLASS</h3>

<p align="center">
  <a href="https://hal.science/view/index/docid/5342486">
    <img src="https://img.shields.io/badge/HAL-5354645-blue?logo=hal" alt="HAL record">
  </a>
  <a href="https://zenodo.org/records/17535167">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.17535167.svg" alt="DOI Zenodo">
  </a>
  <a href="https://monblog.system-linux.fr/RGH-with-grok/">
    <img src="https://img.shields.io/badge/Blog-RGH--with--Grok-orange?logo=blogger" alt="Blog RGH">
  </a>
  <a href="https://github.com/lolotux69/class_public">
    <img src="https://img.shields.io/badge/GitHub-class__public-black?logo=github" alt="GitHub">
  </a>
</p>

---


# Relativité Générale Hypercomplexe (RGH) – Extension de CLASS

## 🪐 Présentation

Ce dépôt contient une version modifiée du code cosmologique **CLASS** (Cosmic Linear Anisotropy Solving System), intégrant la **Relativité Générale Hypercomplexe (RGH)** — une extension quaternionique de la Relativité Générale (RG) proposée par *Laurent Besson (Lolo)*.

Cette approche introduit des composantes hypercomplexes dans le tenseur métrique et explore leurs effets potentiels sur :
- le spectre de puissance linéaire $P(k)$,
- les anisotropies du CMB ($C_\ell^{TT}$),
- les corrections cosmologiques à grande échelle.

Le code permet de comparer directement les modèles **RGH** et **ΛCDM** dans le cadre du formalisme de CLASS.

---

## 📦 Structure du dépôt

```

class_public/
├── source/              # Fichiers C principaux (CLASS)
├── include/             # En-têtes modifiés pour RGH
├── output/              # Résultats des calculs (P(k), C_l, etc.)
├── mon_modele_*.ini     # Fichiers de configuration RGH et LCDM
├── plot_pk.py           # Tracé du spectre de puissance
├── plot_all_clTT.py     # Tracé du spectre CMB TT
├── plot_all_pk_diff.py  # Comparaison RGH vs ΛCDM sur P(k)
├── entete-a-mettre.txt  # En-tête standard Python (config Matplotlib)
└── README.md            # Ce document

````

---

## ⚙️ Installation et environnement

### 1. Création de l’environnement virtuel

```bash
python3 -m venv class_env
source class_env/bin/activate
pip install --upgrade pip
pip install numpy matplotlib PyQt5
````

### 2. Compilation de CLASS

```bash
make clean
make
```

---

## 🚀 Utilisation

### Générer les spectres pour chaque modèle :

```bash
./class mon_modele_LCDM.ini
./class mon_modele_RGH.ini
./class mon_modele_RGH-02.ini
```

Chaque script produit une image .png dans le répertoire courant (par défaut, le dossier racine du projet).

---

## 📊 Visualisation

### 1. Spectre de puissance P(k)

```bash
python3 plot_pk.py
python3 plot_all_pk_diff.py
```

### 2. Spectre CMB TT

```bash
python3 plot_all_clTT.py
```

Chaque script produit une image `.png` dans `output/`.

---

## 🧠 À propos du modèle RGH

* **Idée principale :** remplacer les coordonnées réelles du quadrivecteur par des composantes quaternions hypercomplexes.
* **Objectif :** explorer une extension naturelle de la métrique d’Einstein permettant d’unifier certains effets de jauge et de torsion.

### 🔗 Références :

* [HAL : Relativité Générale Hypercomplexe – Besson, Rahbé (2025)](https://hal.science/view/index/docid/5342486)
* [Zenodo Record](https://zenodo.org/records/17535167)
* [Blog de l’auteur](https://monblog.system-linux.fr/RGH-with-grok/)

---

## 🧩 Exemple de comparaison (visuel)

* `P(k)` : spectre de puissance RGH vs ΛCDM
* `ΔP(k)/P(k)` : différence relative
* `C_ℓ^{TT}` : anisotropies du CMB lissé

Ces sorties permettent de tester la sensibilité cosmologique de la RGH sur les grandes structures.

---

## 🧪 Reproductibilité

Toutes les simulations ont été effectuées sur :

* **Debian 12 (Bookworm)**
* **Python 3.11**
* **Matplotlib ≥ 3.10**
* **CLASS modifié RGH branché sur master**

Les fichiers `.ini` sont compatibles avec CLASS standard, seules les sections RGH ajoutent des paramètres supplémentaires (`alpha_W`, etc.).

---

## 🧾 Licence

Ce travail est distribué sous licence **GPLv3**, conformément à CLASS.

> © 1998–2025 Laurent Besson (Lolo)
> Inspiré du travail collaboratif avec Grok 4.1.2 et GPT-5.

---

## ☕ Contact

* **Auteur :** Laurent Besson
* **Lieu :** Lyon, France
* **Blog :** [monblog.system-linux.fr](https://monblog.system-linux.fr)
