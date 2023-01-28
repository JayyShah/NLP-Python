import pandas as pd
import spacy 
import re
import warnings 
warnings.filterwarnings('ignore')
from spacy import displacy

# Load the IMDB dataset
data = pd.read_csv('../IMDB Dataset.csv')

# Remove special characters and hyperlinks from text
data['review'] = data['review'].str.replace('[^\w\s]','')
data['review'] = data['review'].str.replace('http\S+|www.\S+', '', case=False)

# Load the Spacy model for named entity recognition
nlp = spacy.load("en_core_web_sm")

# Initialize lists to store names and cities
names = []
cities = []

# Iterate through the top 5000 records
for i in range(0, 5000):
    doc = nlp(data.review[i])
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)
        elif ent.label_ == "GPE":
            cities.append(ent.text)

# Create a new dataframe to store the names and cities
entities_df = pd.DataFrame(columns=["Name", "Entity"])
for name in names:
    entities_df = entities_df.append({"Name": name, "Entity": "Person"}, ignore_index=True)
for city in cities:
    entities_df = entities_df.append({"Name": city, "Entity": "City"}, ignore_index=True)

# Convert the dataframe to JSON
entities_json = entities_df.to_json(orient='records')

# Define a function to return the JSON
def get_entities_json():
    return entities_json


