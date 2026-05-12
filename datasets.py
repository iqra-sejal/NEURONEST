#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd
import re


# In[70]:


####################################################   DATASET PHQ-9  ################################################################################


# In[71]:


ds=pd.read_csv(r"D:\uni\AI\aiLab\Dataset_14-day_AA_depression_symptoms_mood_and_PHQ-9.csv")
ds.head(2)


# In[72]:


ds.shape


# In[73]:


ds.isnull().sum()


# In[74]:


print("Total null values:", ds.isnull().sum().sum())


# In[75]:


ds.duplicated().sum()


# In[76]:


ds.describe()


# In[77]:


num_numeric = len(ds.select_dtypes(include=['number']).columns)
num_categorical = len(ds.select_dtypes(include=['object', 'category']).columns)
print(f"Number of numeric columns: {num_numeric}")
print(f"Number of categorical columns: {num_categorical}")


# In[78]:


ds.dtypes


# In[79]:


phq_cols = [f'phq{i}' for i in range(1, 10)]
ds[phq_cols] = ds[phq_cols].fillna(ds[phq_cols].median())

ds['age'] = ds['age'].fillna(ds['age'].median())

ds['sex'] = ds['sex'].fillna(ds['sex'].mode()[0])


# In[80]:


ds.isnull().sum()


# In[81]:


q_cols = [col for col in ds.columns if col.startswith('q') and ds[col].dtype != 'object']

for col in q_cols:
    ds[col] = ds[col].fillna(ds[col].median())


# In[82]:


ds.isnull().sum()


# In[83]:


ds.duplicated().sum()


# In[84]:


print("Total null values:", ds.isnull().sum().sum())


# In[85]:


numeric_cols = ds.select_dtypes(include=['number'])
corr_matrix = numeric_cols.corr()
print(corr_matrix)



# In[86]:


import seaborn as sns
import matplotlib.pyplot as plt

numeric_cols = ds.select_dtypes(include=['number']).columns

plt.figure(figsize=(12, 6))
sns.boxplot(data=ds[numeric_cols])
plt.title('Outliers')
plt.xticks(rotation=45)
plt.show()


# In[87]:


numeric_cols = ds.select_dtypes(include=['number'])

long_df = numeric_cols.melt(var_name='Column', value_name='Value')

plt.figure(figsize=(15, 6))
sns.stripplot(data=long_df, x='Column', y='Value', jitter=True, alpha=0.5)

plt.title('Outliers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:





# In[88]:


ds.to_excel("phq_cleaned_dataset.xlsx", index=False)


# In[89]:


########################################   DATASET TEXT ( for sentiment analysis )   ##############################################################3


# In[90]:


get_ipython().system('pip install sentence_transformers')


# In[91]:


from sentence_transformers import SentenceTransformer
import re


# In[95]:


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


# In[ ]:





# In[98]:


dt=load_and_preprocess_dataset()
print(dt.columns)


# In[ ]:




