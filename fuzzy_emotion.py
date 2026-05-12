#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install scikit-fuzzy')


# In[14]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from textblob import TextBlob

# Define fuzzy variables
polarity = ctrl.Antecedent(np.arange(-1, 1.01, 0.01), 'polarity')
subjectivity = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'subjectivity')
emotion = ctrl.Consequent(np.arange(0, 101, 1), 'emotion')

# Membership functions for polarity
polarity['negative'] = fuzz.trimf(polarity.universe, [-1, -1, 0])
polarity['neutral'] = fuzz.trimf(polarity.universe, [-0.1, 0, 0.1])
polarity['positive'] = fuzz.trimf(polarity.universe, [0, 1, 1])

# Membership functions for subjectivity
subjectivity['low'] = fuzz.trimf(subjectivity.universe, [0, 0, 0.5])
subjectivity['medium'] = fuzz.trimf(subjectivity.universe, [0.2, 0.5, 0.7])
subjectivity['high'] = fuzz.trimf(subjectivity.universe, [0.7, 1, 1])


# Membership functions for emotion score
emotion['depressed'] = fuzz.trimf(emotion.universe, [0, 10, 25])
emotion['worried'] = fuzz.trimf(emotion.universe, [20, 35, 50])
emotion['angry'] = fuzz.trimf(emotion.universe, [40, 55, 70])
emotion['sad'] = fuzz.trimf(emotion.universe, [30, 45, 60])
emotion['calm'] = fuzz.trimf(emotion.universe, [50, 60, 70])
emotion['content'] = fuzz.trimf(emotion.universe, [70, 80, 90])
emotion['excited'] = fuzz.trimf(emotion.universe, [85, 95, 100])

# Define fuzzy rules
rules = [
    ctrl.Rule(polarity['negative'] & subjectivity['high'], emotion['depressed']),
    ctrl.Rule(polarity['negative'] & subjectivity['medium'], emotion['worried']),
    ctrl.Rule(polarity['negative'] & subjectivity['low'], emotion['angry']),

    ctrl.Rule(polarity['neutral'] & subjectivity['low'], emotion['calm']),
    ctrl.Rule(polarity['neutral'] & subjectivity['medium'], emotion['sad']),

    ctrl.Rule(polarity['positive'] & subjectivity['low'], emotion['calm']),
    ctrl.Rule(polarity['positive'] & subjectivity['medium'], emotion['content']),
    ctrl.Rule(polarity['positive'] & subjectivity['high'], emotion['excited'])
]

# Create control system
emotion_ctrl = ctrl.ControlSystem(rules)
emotion_sim = ctrl.ControlSystemSimulation(emotion_ctrl)

def analyze_emotion_fuzzy(user_text):
    blob = TextBlob(user_text)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity

    # Expanded list of high-energy / joyful keywords
    high_energy_keywords = [
        "dance", "dancing", "celebrate", "celebrating", "laugh", "laughing",
        "joy", "joyful", "happy", "happiness", "smile", "smiling",
        "excited", "exciting", "amazing", "awesome", "great", "wonderful",
        "love", "blessed", "fantastic", "cheerful", "vibrant", "delighted",
        "thrilled", "pumped", "energetic", "fun", "ecstatic", "overjoyed", "elated"
    ]

    text_lower = user_text.lower()
    high_energy_match = sum(word in text_lower for word in high_energy_keywords)

    if high_energy_match >= 3:
        return 95, "excited"

   # if high_energy_match >= 1:
    #    polarity_score = min(1.0, polarity_score + 0.2)
     #   subjectivity_score = min(1.0, subjectivity_score + 0.2)

   # if polarity_score > 0.8 and subjectivity_score > 0.8:
    #    return 95, "excited"

    emotion_sim.input['polarity'] = polarity_score
    emotion_sim.input['subjectivity'] = subjectivity_score
    emotion_sim.compute()

    score = emotion_sim.output['emotion']
    fuzzy_label = classify_emotion(score)

    return score, fuzzy_label
def status_to_fuzzy(severity):
    mapping = {
        "minimal": "content",
        "mild": "worried",
        "moderate": "sad",
        "moderately severe": "angry",
        "severe": "depressed"
    }
    return mapping.get(severity.lower(), "calm")


def classify_emotion(score):
    if score < 20:
        return "depressed"
    elif score < 35:
        return "worried"
    elif score < 50:
        return "sad"
    elif score < 65:
        return "angry"
    elif score < 75:
        return "calm"
    elif score < 93:
        return "content"
    else:
        return "excited"

if __name__ == "__main__":
    text = "I'm feeling great today"
    score, label = analyze_emotion_fuzzy(text)
    print(f"Fuzzy Emotion Score: {score:.2f}")
    print(f"Detected Emotion: {label}")


# In[ ]:





# In[ ]:




