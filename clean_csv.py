import pandas as pd
import json

# This script iterates over a csv of toponymic data and extracts toponyms containing the words in the json list

df = pd.read_csv('toponyms.csv', encoding='latin1') # Change encoding if needed
df.drop_duplicates()

with open('./quechua_terms.json') as file:
    terms = json.load(file)

for term in terms:
     df[df['Name'].str.lower().str.contains(tern)].to_csv('topo-quechua\{0}.csv'.format(term), encoding='latin1')