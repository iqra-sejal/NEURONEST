#!/usr/bin/env python
# coding: utf-8

# In[5]:


import joblib
import numpy as np


# In[6]:


# Load PHQ9 model
phq9_model = joblib.load('decision_tree_model.pkl')

# Load text classification model
text_model = joblib.load('text_random_forest_model.pkl')


# In[7]:


def predict_severity(phq_scores):
    if len(phq_scores) != 9:
        raise ValueError("Exactly 9 PHQ responses are required.")
    input_array = np.array(phq_scores).reshape(1, -1)
    prediction = phq9_model.predict(input_array)[0]
    return prediction


# In[ ]:





# In[ ]:





# In[8]:


import fuzzy_emotion
import numpy as np
import joblib
from sentence_transformers import SentenceTransformer

# Global variables to cache model & SBERT encoder
text_model = None
sbert_model = None

def predict_user_text(text):
    global text_model, sbert_model  # Needed to assign to the global ones

    # Lazy-load the model once
    if text_model is None:
        text_model = joblib.load("D:/uni/AI/aiLab/text_random_forest_model.pkl")

    if sbert_model is None:
        sbert_model = SentenceTransformer('all-MiniLM-L6-v2')

    # Create embedding & predict
    embedding = sbert_model.encode([text])
    predicted_status = text_model.predict(embedding)[0]

    # Fuzzy logic classification from predicted class
\
   # fuzzy_emotion.emotion_sim.compute()

   # fuzzy_from_classifier = fuzzy_emotion.classify_emotion(fuzzy_emotion.emotion_sim.output['emotion'])

    # Fuzzy classification from text
    _, fuzzy_from_text = fuzzy_emotion.analyze_emotion_fuzzy(text)

    return predicted_status, fuzzy_from_text


if __name__ == "__main__":
    text = "I'm feeling great today, everything and every work of mine is falling into place and I can't stop smiling. I just want to laugh and dance and celebrate, also today I am going for dinner with my love which I cannot wait for!"
    emo= predict_user_text(text)
    print(f"Fuzzy Emotion : {emo}")



# In[ ]:





# In[ ]:





# In[18]:


"""
import numpy as np
import joblib
from sentence_transformers import SentenceTransformer

# Load model and SBERT
model = joblib.load("D:/uni/AI/aiLab/text_random_forest_model.pkl")
sbert_model = SentenceTransformer('all-MiniLM-L6-v2')  # Make sure you use the same model as in training

def predict_user_text(user_text):
    # Get SBERT embedding for the input text
    embedding = sbert_model.encode([user_text])  
    # Predict the label using the trained model
    pred_label = model.predict(embedding)[0]  # Returns string label like 'Depression', 'Stress', etc.
    
    return pred_label

# Example usage:
user_journal = "i am sick and tired of my life, i have tried everything in my life to make it better ,but now enough "
prediction = predict_user_text(user_journal)
print("Prediction:", prediction)
"""


# In[ ]:




