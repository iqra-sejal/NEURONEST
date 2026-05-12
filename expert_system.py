#!/usr/bin/env python
# coding: utf-8

# In[1]:


import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
from experta import *


# In[1]:


# expert_system.py
class MentalHealthAdvisor:
    def __init__(self):
        # You can later expand with more complex rules, databases, or fuzzy reasoning
        pass

    def give_advice(self, severity):
        if severity == "Severe":
            return "Please seek professional mental health support immediately."
        elif severity == "Moderately Severe":
            return "Consider scheduling a consultation with a therapist."
        elif severity == "Moderate":
            return "Monitor your mood closely and try self-help strategies."
        elif severity == "Mild":
            return "Engage in relaxing activities and maintain social contact."
        else:
            return "Keep up healthy habits and regular check-ins."


# In[4]:


import random

# Function to return background music filename based on emotion
def get_background_music(emotion):
    music = {
        "depressed": "calm_piano.mp3",
        "worried": "soothing_ambient.mp3",
        "angry": "soft_jazz.mp3",
        "sad": "uplifting_strings.mp3",
        "calm": "nature_sounds.mp3",
        "content": "happy_ukulele.mp3",
        "excited": "party_pop.mp3"
    }
    return music.get(emotion, "default_background.mp3")

# Function to return motivational quote based on emotion
def get_motivational_quote(emotion):
    quotes = {
        "depressed": [
            "This too shall pass.",
            "You are stronger than you think.",
            "Your story isn’t over yet."
        ],
        "worried": [
            "Focus on what you can control.",
            "You have survived 100% of your worst days.",
            "Worrying means you care – that’s your strength."
        ],
        "angry": [
            "Breathe. You are in control.",
            "Anger is one letter short of danger.",
            "Turn your frustration into motivation."
        ],
        "sad": [
            "Crying is how your heart speaks when your lips can't explain.",
            "Storms don’t last forever.",
            "Sadness is a part of healing."
        ],
        "calm": [
            "Peace is always beautiful.",
            "Stillness speaks louder than words.",
            "Take this moment to be fully present."
        ],
        "content": [
            "Gratitude turns what we have into enough.",
            "Happiness grows where you water it.",
            "Appreciate this calm moment."
        ],
        "excited": [
            "Let the excitement flow through you!",
            "Your energy is contagious. Embrace it.",
            "Today is yours—make it legendary!"
        ]
    }
    return random.choice(quotes.get(emotion, ["Keep going, you're doing great!"]))

# Function to return dashboard theme based on emotion
def get_dashboard_theme(emotion):
    themes = {
        "depressed": "theme_skyblue",     # soothing blue shades
        "worried": "theme_mint",          # cool, relaxing greens
        "angry": "theme_coolgray",        # neutral, calming tones
        "sad": "theme_purple",            # soft violet shades
        "calm": "theme_green",            # earthy, relaxing greens
        "content": "theme_orange",        # cheerful, light theme
        "excited": "theme_yellow"         # bright and energetic
    }
    return themes.get(emotion, "theme_default")

# Function to suggest an activity based on emotion
def get_activity_suggestion(emotion):
    suggestions = {
        "depressed": "Try a 10-minute walk outside to boost your mood.",
        "worried": "Write down your thoughts to clear your mind.",
        "angry": "Squeeze a stress ball or do breathing exercises.",
        "sad": "Watch a comforting movie or talk to someone you trust.",
        "calm": "Practice mindfulness or light stretching.",
        "content": "Write in your gratitude journal or draw something.",
        "excited": "Dance to your favorite song or make a to-do list!"
    }
    return suggestions.get(emotion, "Take a few deep breaths and relax.")

# Main expert system decision function
def run_expert_system(emotion, severity):
    response = {
        "background_music": get_background_music(emotion),
        "motivational_quote": get_motivational_quote(emotion),
        "dashboard_theme": get_dashboard_theme(emotion),
        "activity_suggestion": get_activity_suggestion(emotion),
        "severity_level": severity
    }

    # Add extra support if severity is high
    if severity in ["moderate", "moderately severe", "severe"]:
        response["extra_support"] = (
            "It may be helpful to talk to a counselor or mental health professional. "
            "You're not alone, and support is available."
        )

    return response

# Example test (can be removed in integration)
if __name__ == "__main__":
    example_emotion = "worried"
    example_severity = "moderate"
    output = run_expert_system(example_emotion, example_severity)
    
    for key, value in output.items():
        print(f"{key}: {value}")


# In[ ]:




