# BDA_ProjGrB

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
