# BDA_ProjGrB
## Phase3
### Description of the features used and any pre-processing to extract additional features

Sur les 19 features présentes dans le dataset, nous avons choisi de conserver les suivantes :

- tpep_pickup_datetime : Date et heure de mise en service du compteur.
- tpep_dropoff_datetime : Date et heure d'arrêt du compteur.
- passenger_count : Nombre de passagers dans le véhicule.
- trip_distance : Distance parcourue, en miles, indiquée par le taximètre.
- PULocationID : Zone TLC Taxi où le taximètre a été activé.
- DOLocationID : Zone TLC Taxi où le taximètre a été arrêté.
- payment_type : Code numérique indiquant le mode de paiement du passager (1 = carte de crédit, 2 = espèces, 3 = sans frais, 4 = litige, 5 = inconnu, 6 = voyage annulé).
- tip_amount : Montant du pourboire, automatiquement renseigné pour les paiements par carte (les pourboires en espèces ne sont pas inclus).
- total_amount : Montant total facturé aux passagers (ne comprend pas les pourboires en espèces).

Les features suivantes ont été exclues pour diverses raisons :

- RatecodeID, store_and_fwd_flag, congestion_surcharge, et Airport_fee présentaient une grande proportion de valeurs manquantes, comme observé dans le fichier Exploration_data.ipynb.
- fare_amount, extra, mta_tax, tolls_amount, et improvement_surcharge sont des composantes déjà incluses dans total_amount.
- VendorID ne nous est pas utile pour les questions posées, car il s'agit simplement du fournisseur TPEP qui a généré l'enregistrement.

### Goals of the analysis

L'objectif principal est de nettoyer les données pour assurer des résultats pertinents lors de la phase 4. Dans le fichier Cleaning_yellow_taxi_trip.zpln, j'ai effectué les traitements suivants :

- Filtré tpep_pickup_datetime et tpep_dropoff_datetime pour garder les années entre 2013 et 2023, en éliminant les valeurs aberrantes telles que les années 2001, 2004 et 2011.
- Supprimé les lignes avec des passenger_count manquants ou inférieurs à 1.
- Conservé les trip_distance supérieures à 0 et inférieures à 800 miles.
- Assuré que le payment_type soit compris entre 1 et 6.
- Garanti que le tip_amount soit égal ou supérieur à 0.
- Limité le total_amount à un intervalle supérieur à 0 mais inférieur à 400 dollars.
- Vérifié que les PULocationID et DOLocationID correspondent à des valeurs entre 1 et 265, qui sont les zones valides de New York (consultables dans le fichier taxi_zone_lookup.csv).

Cleaning_yellow_taxi_trip.zpln a été préparé suite à une exploration initiale des données réalisée dans Exploration_yellow_taxi_trip.zpln, qui a servi de brouillon pour cette phase.

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

#### Est-possible de prédire les pourboires en fonction du quartier de départ ?

**Approche initiale pour résoudre la question :**
-Utiliser les données historiques sur les pourboires et les lieux de départ des trajets.

- Développer un modèle prédictif (par exemple, régression linéaire, arbre de décision) pour estimer les pourboires en fonction du quartier de départ. L'analyse exploratoire peut aider à identifier d'autres variables pertinentes (durée du trajet, heure du jour, jour de la semaine vs weekend, etc.).

### Un script pour télécharger l'ensemble des données

Voir le fichier : script_download.py

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
