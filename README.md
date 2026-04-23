 # Assistant de Mobilité Intelligente - Cotonou Smart City

## Présentation du Projet
Ce projet vise à optimiser la mobilité urbaine à Cotonou (Bénin) en proposant un outil d'aide à la décision basé sur la Data Science. L'application prédit le temps de trajet et évalue le risque d'accident en fonction de variables contextuelles comme la météo, l'heure de pointe et le mode de transport.

L'objectif est d'aider les citoyens à arbitrer entre rapidité et sécurité, particulièrement lors des épisodes de fortes pluies ou de congestion routière.

## Fonctionnalités Clés
* Prédiction Temporelle : Estimation de la durée du trajet via un modèle de régression Random Forest.

* Analyse de Sécurité : Calcul d'un score de risque d'accident personnalisé selon le mode de transport (Zemidjan, Voiture, Bus).

* Cartographie Interactive : Visualisation des points de départ et d'arrivée sur une carte interactive via Folium.

* Interface Intuitive : Dashboard dynamique développé avec Streamlit.

## Architecture Technique
Le projet suit une pipeline Data Science complète :

* Exploration des données (EDA) : Analyse des corrélations entre trafic, météo et accidents.

* Prétraitement : Encodage des variables catégorielles et standardisation des caractéristiques numériques.

* Modélisation : Utilisation du RandomForestRegressor pour sa robustesse face aux relations non-linéaires.

* Géospatial : Structuration des quartiers de Cotonou avec GeoPandas.

## Structure du Dépôt
app.py : Code principal de l'application Streamlit.

analyse_eda.py : Script de génération des analyses visuelles.

model_duree.pkl / model_risque.pkl : Modèles de Machine Learning entraînés.

cotonou_points.geojson : Données géospatiales des quartiers de Cotonou.

requirements.txt : Liste des dépendances Python.

## Installation Locale
Pour exécuter ce projet sur votre machine :

Cloner le dépôt :

Bash
git clone https://github.com/Oluwatoyinandil/cotonou-mobility-app.git
cd cotonou-mobility-app
Installer les dépendances :

Bash
pip install -r requirements.txt
Lancer l'application :

Bash
streamlit run app.py

## Résultats & Conclusions
L'analyse a révélé que :

* La Forte Pluie augmente le temps de trajet de manière significative (jusqu'à +60%).

* Le Zem (moto) présente un risque d'accident 4 fois supérieur aux autres modes en cas d'intempéries.

* L'indice de trafic reste le facteur dominant durant les heures de pointe (7h-9h / 17h-19h).

