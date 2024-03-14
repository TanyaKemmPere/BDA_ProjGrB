# BDA_ProjGrB

A README.md file (section phase 1) with the description (size, schema, datatypes, etc) and link of the chosen datasets (First, second and third choice) 

## 1e choice: New-york Taxi Trip Data
https://www.kaggle.com/datasets/microize/newyork-yellow-taxi-trip-data-2020-2019

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

## autre solution pour le dataset :
site officiel : https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page / https://www.kaggle.com/datasets/microize/nyc-taxi-dataset
(fichier en format PARQUET et non CSV depuis mai/2022 = fichiers moins lourds et plus rapides)
La conséquence serait de prendre les données mensuels dans un intervalle de temps pour les taxis jaunes pour arriver en dessous de 20 GB
Estimation du volume de stockage des fichiers PARQUET par année -> 2009 : 5.7 GB, 2010 : 5.6 GB, 2011 : 2.2 GB, 2012 : 2.1 GB, 2013 : 2.1 GB, 2014 : 2.1 GB, 2015 : 2 GB, 2016 : 1.8 GB, 2017 : 1.5 GB, 2018 : 1.4 GB, 2019 : 1.2 GB, 2020 : 0.3 GB, 2021 : 0.4 GB, 2022 : 0.6 GB, 2023 : 0.6 GB


## 2e choice: Brewery Operations and Market Analysis Dataset
https://www.kaggle.com/datasets/ankurnapa/brewery-operations-and-market-analysis-dataset

### Size
2.62 GB

### Content
- Brewing Parameters
- Beer Styles and Packaging
- Quality Scores
- Sales Data(USD)
- Supply Chain and Efficiency Metrics
- Applications
- Brewing Process Optimization
- Market Analysis
- Supply Chain Management
- Quality Assessment and Control
- Data Format and Structure

## 3e choice: 
