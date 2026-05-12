# 🧠 NEURONEST

### AI-Based Hybrid Mental Health Assessment System

---

## 📌 Overview

**NEURONEST** is a multi-modal AI-based mental health assessment system that integrates **machine learning, natural language processing, computer vision, fuzzy logic, and expert systems** to evaluate a user’s mental well-being.

The system allows users to assess their mental health through:

* PHQ-9 questionnaire
* Journal-based text input
* Facial emotion detection

It then provides **personalized suggestions, motivational support, and mood-based interactions** through an interactive GUI.

---

## 🎯 Objectives

* Develop a **multi-modal mental health evaluation system**
* Implement:

  * Decision Tree for PHQ-9 analysis
  * Random Forest + SBERT for text analysis
  * CNN for facial emotion recognition
  * Fuzzy Logic for uncertainty handling
  * Rule-based Expert System for recommendations
* Build a user-friendly GUI using Tkinter

---

## 🚀 Key Features

### 📝 PHQ-9 Depression Detection

* Uses **Decision Tree Classifier**
* Input: 9 questionnaire responses
* Output:

  * Minimal
  * Mild
  * Moderate
  * Moderately Severe
  * Severe

---

### 💬 Journal-Based Sentiment Analysis

* Uses:

  * **SBERT embeddings**
  * **Random Forest Classifier**
  * **TextBlob (polarity & subjectivity)**
* Enhanced with **Fuzzy Logic** for emotion classification

---

### 😊 Facial Emotion Recognition

* Built using **Convolutional Neural Network (CNN)**
* Detects emotions:

  * Happy, Sad, Angry, Fearful, Neutral, etc.
* Supports:

  * Image upload
  * Real-time webcam capture

---

### 🧠 Fuzzy Logic System

* Handles uncertain emotional states
* Uses:

  * Polarity
  * Subjectivity
* Outputs refined emotional categories like:

  * Depressed
  * Worried
  * Calm
  * Content
  * Excited

---

### 🤖 Expert System

* Rule-based decision system
* Combines:

  * PHQ-9 severity
  * Text emotion
  * Facial emotion
* Provides:

  * Personalized suggestions
  * Motivational quotes
  * Mood-based themes
  * Music recommendations

---

### 🖥️ GUI Application

* Built with **Tkinter**
* Includes:

  * Multi-screen navigation
  * Breathing exercise module
  * Emotion-based UI changes

---

## 🏗️ System Workflow

```text
User Input (PHQ-9 / Text / Image)
        ↓
Data Preprocessing
        ↓
ML Models (Decision Tree + Random Forest + CNN)
        ↓
Fuzzy Logic Processing
        ↓
Expert System
        ↓
Personalized Output (Advice + Theme + Music)
```

---

## 🛠️ Technologies Used

* **Programming:** Python
* **Machine Learning:** Scikit-learn
* **Deep Learning:** TensorFlow / Keras
* **NLP:** SBERT, TextBlob
* **Computer Vision:** OpenCV
* **Fuzzy Logic:** scikit-fuzzy
* **GUI:** Tkinter

---



## ⚙️ Installation

```bash
git clone https://github.com/iqra-sejal/NEURONEST.git
cd NEURONEST
pip install -r requirements.txt
python src/main_gui.py
```

---

## 📦 Model Files

Large trained models are not included due to GitHub size limits.
👉 Download from:
*(https://drive.google.com/file/d/1XdLYOxrjIR4uJkOFmpCp_TevdKNI4cUS/view?usp=drive_link)*

*(https://drive.google.com/file/d/1k2CWKq51_sRztkqnQlNXyZvPYJGqDl1u/view?usp=drive_link)*

---

## 🔮 Future Enhancements

* Voice-based emotion detection
* Web deployment
* Mobile application integration
* Larger and diverse datasets
* Real-time continuous monitoring

---

## ⚠️ Disclaimer

This system is **not a medical diagnostic tool**.
It is intended for **educational and awareness purposes only**.

---



## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
