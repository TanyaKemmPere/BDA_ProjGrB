# BDA_ProjGrB

## Phase2

### Le choix du jeu de données, la justification basée sur la taille, l'exhaustivité et la qualité des données

Nous avons décidé d'utiliser pour le projet le jeu de données _New York Taxi Trip Data_ (Yellow Taxi Trip Records). Les données seront téléchargées directement depuis le site officiel : https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page. Pour la période de 2013 à 2023, cela représente environ 14 Go de fichiers organisés par mois et par année, au format parquet.
Après avoir exploré ces données, nous constatons que le jeu de données New York Taxi Trip Data est de qualité et de quantité suffisantes pour répondre à nos questions de recherche et satisfaire les exigences du projet.
Le dataset contient quelques valeurs aberrantes qui devront être supprimées mais il ne semble pas contenir de valeurs nulles dans les champs que nous identifions comme utiles à notre projet.(cf. Exploration_data.ipynb).

### Questions définies

#### Comment la pandémie de COVID-19 a-t-elle affecté l'industrie du taxi ? (nombre de courses, quels quartiers sont les plus impactés, ...)

**Approche initiale pour résoudre la question :**

- Utiliser les données de taxi pour comparer le volume de courses avant et pendant la pandémie.
- Analyser les variations géographiques pour identifier les quartiers les plus impactés. L'intégration de données démographiques ou économiques peut aussi aider à contextualiser les changements observés.

#### Quel est l'impact des conditions météorologiques sur la fréquence des trajets en taxi ? (utilisation d'un autre jeu de données métérologique en parallèle)

**Approche initiale pour résoudre la question :**

- Fusionner les données météorologiques avec les données de taxi sur la même période.
- Examiner comment les variations de la météo (pluie, température) influencent la demande de taxis.
- Utiliser des analyses statistiques pour évaluer la corrélation entre la météo et le nombre de courses.

#### Quelles sont les zones de départ et d'arrivée les plus fréquentes pour les trajets en taxi ?

**Approche initiale pour résoudre la question :**

- Analyser des données de localisation pour identifier les points de ramassage et de dépose les plus communs.
- Les visualisations comme les cartes de chaleur peuvent être utiles pour illustrer ces tendances.

#### Quels sont les types de trajets les plus rentables pour les chauffeurs de taxi ? (en tenant compte des pourboires, des distances et des tarifs)

**Approche initiale pour résoudre la question :**

- Examiner les données sur les pourboires, les tarifs, les distances, et les durées des trajets. Crée des catégories de trajets (par exemple, court/moyen/long) et analyse les bénéfices moyens par catégorie.
- Utiliser des techniques d'analyse multivariée (clustering) pour déterminer les facteurs qui maximisent les revenus des chauffeurs.

#### Quelles sont les heures pour lesquels les trajets sont les plus courts ?

**Approche initiale pour résoudre la question :**

- Collecter des données sur la durée des trajets et les horaires correspondants.
- Analyser les périodes de la journée pour identifier les moments où les trajets sont généralement plus courts, probablement en raison de moins de trafic. La visualisation des données horaires peut révéler des tendances claires.

#### Est-possible de prédire les pourboires en fonction du quartier de départ ?

**Approche initiale pour résoudre la question :**
-Utiliser les données historiques sur les pourboires et les lieux de départ des trajets.

- Développer un modèle prédictif (par exemple, régression linéaire, arbre de décision) pour estimer les pourboires en fonction du quartier de départ. L'analyse exploratoire peut aider à identifier d'autres variables pertinentes (durée du trajet, heure du jour, jour de la semaine vs weekend, etc.).

### Un script pour télécharger l'ensemble des données

Nous n’avons pas créé un script de téléchargement pour les données car nous sommes passés par le site web officiel. Dans le cas où on ferait trop de requêtes, on risque de se faire bannir du site.

### Script de traitement des données et résultats

Voir le fichier : exploration_data.ipynb

## Phase1

## Choice 1: Newyork Taxi Trip Data

https://www.kaggle.com/datasets/microize/newyork-yellow-taxi-trip-data-2020-2019
The New York Taxi Trip Data offers detailed insights into taxi trips within NYC, including temporal and spatial dimensions, trip metrics, fare details, and passenger information.

### Size

9.36 GB (fichiers CSV)

### Content

- VendorID: Int
- tpep_pickup_datetime: Date/Time
- tpep_dropoff_datetime: Date/Time
- Passenger_count: Int
- Trip_distance: Float
- PULocationID: Int
- DOLocationID: Int
- RateCodeID: Int
- Store_and_fwd_flag: String
- Payment_type: Int
- Fare_amount: Float
- Extra: Float
- MTA_tax: Float
- Improvement_surcharge: Float
- Tip_amount: Float
- Tolls_amount: Float
- Total_amount: Float

### others options:

site officiel: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page / https://www.kaggle.com/datasets/microize/nyc-taxi-dataset
(fichier en format PARQUET et non CSV depuis mai/2022 = fichiers moins lourds et plus rapides)
La conséquence serait de prendre les données mensuels dans un intervalle de temps pour les taxis jaunes pour arriver en dessous de 20 GB.

Estimation du volume de stockage des fichiers PARQUET par année -> 2009 : 5.7 GB, 2010 : 5.6 GB, 2011 : 2.2 GB, 2012 : 2.1 GB, 2013 : 2.1 GB, 2014 : 2.1 GB, 2015 : 2 GB, 2016 : 1.8 GB, 2017 : 1.5 GB, 2018 : 1.4 GB, 2019 : 1.2 GB, 2020 : 0.3 GB, 2021 : 0.4 GB, 2022 : 0.6 GB, 2023 : 0.6 GB

## Choice 2: Brewery Operations and Market Analysis Dataset

https://www.kaggle.com/datasets/ankurnapa/brewery-operations-and-market-analysis-dataset

### Size

2.62 GB

### Schema

- Brewing Parameters: fermentation time, temperature, pH level, gravity, ingredient ratios
- Beer Styles and Packaging: IPA, Stout, Lager, etc., packaged in kegs, bottles, cans, pints
- Quality Scores: Ratings on a scale, reflecting batch quality
- Sales Data(USD): Records of sales figures across various locations in Bangalore
- Supply Chain and Efficiency Metrics: Volume produced, total sales, brewhouse efficiency, losses at different stages

### Data types

- Brewing Parameters: Float
- Beer Styles, Packaging: Categorical
- Quality Scores: Integer
- Sales Data: Float (USD)
- Supply Chain Metrics: Float

## Choice 3: M5 Forecasting - Accuracy

https://www.kaggle.com/competitions/m5-forecasting-accuracy/data
The M5 Forecasting - Accuracy dataset involves forecasting unit sales of various products sold in the USA by Walmart. It provides hierarchical sales data covering stores in California, Texas, and Wisconsin. The dataset includes item-level, department, product category, and store details, along with explanatory variables such as price, promotions, day of the week, and special events.

### Size

450.47 MB

### Content

- calendar.csv: Information about the dates of product sales
- sales_train_validation.csv: Historical daily unit sales data per product and store (d_1 - d_1913)
- sample_submission.csv: Correct format for submissions
- sell_prices.csv: Information about the price of products sold per store and date
- sales_train_evaluation.csv: Includes sales (d_1 - d_1941) (labels used for the Public leaderboard)
