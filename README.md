# 📊 Visualisation System

**Visualisation System** est une application développée en Python avec **Streamlit** qui permet de visualiser facilement les indicateurs de performance d’un système de recommandation. Elle complète l'**Application 1 : Performance System** en proposant une interface interactive pour analyser les résultats générés, par catégorie d'indicateurs et par cluster d'utilisateurs.

---

## 🎯 Objectifs

- Charger des fichiers JSON contenant les résultats de performance d’un système de recommandation.
- Organiser les données par **catégorie d’indicateurs** et par **cluster d’utilisateurs**.
- Proposer des **visualisations interactives** (graphiques, tableaux) pour faciliter l’analyse et l’interprétation.
- Comparer les indicateurs entre clusters pour détecter des tendances ou inégalités de performance.

---

## 📁 Données attendues

L'application prend en entrée des fichiers JSON générés par l'application Performance System.

---

### Exemple de structure :
```json
{
  "metadata": {
    "date": "2025-03-17",
    "mode": "cluster",
    "indicateurs": ["Precision@k", "Recall@k", "MAE", "RMSE"]
  },
  "résultats": {
    "cluster_1": {
      "Precision@k": 0.78,
      "Recall@k": 0.65,
      "MAE": 0.32,
      "RMSE": 0.45
    },
    "cluster_2": {
      "Precision@k": 0.85,
      "Recall@k": 0.70,
      "MAE": 0.29,
      "RMSE": 0.40
    }
  }
}
```
---
## Fonctionnalités principales
Chargement de fichiers JSON via l’interface.

Sélection des catégories d’indicateurs : Précision, Couverture, Personnalisation/Diversité, Nouveauté, Robustesse.

Affichage interactif des indicateurs sous forme :

de graphiques en barres

de courbes (lignes)

de diagrammes en camembert

de tableaux numériques

Comparaison entre clusters pour chaque indicateur sélectionné.

---

## 🛠️ Technologies utilisées

* Streamlit : Interface web interactive
* Matplotlib : Génération de graphiques
* NumPy : Traitement numérique
* Pandas : Manipulation de données
* JSON : Format des fichiers d’entrée

--- 

## 🚀 Lancer l'application
* Cloner le dépôt
git clone https://github.com/ton-compte/visualisation-system.git
cd visualisation-system

* Installer les dépendances
pip install -r requirements.txt

* Lancer Streamlit
streamlit run App.py

---

## Structure du projet

├── App.py                    
├── data/
│   └── results.json          
├── utils/                    
├── requirements.txt          
└── README.md            

---

## 👥 Auteurs
Louise Amedjkane

Hawa Diabate

Sabah Hamouta

Projet universitaire – Mars 2025
Nom du projet : Systèmes de Recommandation