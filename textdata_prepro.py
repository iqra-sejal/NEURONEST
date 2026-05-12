#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!pip install sentence_transformers


# In[8]:


import pandas as pd
from sentence_transformers import SentenceTransformer
import re


# In[3]:


sbert_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def preprocess_text(text):
    """
    Clean the input text (lowercase, remove punctuation, etc.)
    """
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@w+|\#', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_sbert_embedding(text):
    """
    Get SBERT embedding for the cleaned text
    """
    cleaned_text = preprocess_text(text)
    embedding = sbert_model.encode(cleaned_text)
    return embedding



def load_and_preprocess_dataset(path=r"D:\uni\AI\aiLab\textbased_dataset.csv"):
    df = pd.read_csv(path)
    df.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore') 
    df.dropna(axis=0, inplace=True)

    # Preprocess the text column
    df['statement'] = df['statement'].apply(preprocess_text)
    
    return df


# In[9]:


dt=load_and_preprocess_dataset()
print(dt.columns)


# In[ ]:





# In[ ]:




