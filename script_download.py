import requests
import os
from concurrent.futures import ThreadPoolExecutor

def download_file(url, file_name, directory):
    os.makedirs(directory, exist_ok=True)
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(directory, file_name), 'wb') as file:
            file.write(response.content)
        print(f"Téléchargé {file_name}")
    else:
        print(f"Impossible de télécharger {file_name}")

def download_yellow_taxi_data(start_year=2013, end_year=2023, data_directory='data'):
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
    with requests.Session() as session, ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                file_name = f"yellow_tripdata_{year}-{month:02d}.parquet"
                url = f"{base_url}{file_name}"
                future = executor.submit(download_file, url, file_name, data_directory)
                futures.append(future)
        
        for future in futures:
            future.result()

data_directory = 'C:\\Users\...\\data'  # Créer un dossier data et donner le chemin d'où il a été créé
download_yellow_taxi_data(data_directory=data_directory)













