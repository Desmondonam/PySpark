import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

file_url = 'https://api.slingacademy.com/v1/sample-data/files/salaries.csv'

df = pd.read_csv(file_url, storage_options={
                        'User-Agent': 'Mozilla/5.0'})

# 5 first rows
print(df.head())