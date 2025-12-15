🧠 MindMate Harmony Space
AI Mental-Wellbeing Companion powered by Jaseci & Object-Spatial Programming (OSP)
📖 Overview

MindMate Harmony Space is an AI-driven digital companion designed to help users track their emotional wellbeing, identify triggers, and receive personalized coping strategies.

This project was built for the AI Hackathon to showcase how the Object-Spatial Graph (OSP) can represent and analyze emotional states, mood patterns, and their underlying triggers.

MindMate acts as a supportive companion that lets users:

Log their daily moods

Understand emotional patterns

Detect repeating triggers

Receive personalized AI-generated mental health advice

Key Features
Mood Logging

Users input a mood score (1–10) and describe what they're feeling.

OSP Graph Emotional Logic

The backend constructs a dynamic emotional graph:

emotion_entry nodes store mood records

trigger nodes store emotional triggers

triggered_by edges connect moods to their causes

AI Therapist Agent

A specialized walker analyzes the graph and generates supportive, empathetic advice based on recent emotional activity.

Multi-Agent System

Logger Agent – Handles mood creation

Therapist Agent – Performs emotional analysis

Pattern Recognition

Common triggers and recurring mood trends become visible through OSP graph traversal.

Tech Stack
Layer	Technology
Backend	Jaseci (Jac Language)
Frontend	Streamlit (Python)
Architecture	Multi-Agent System (Logger + Therapist)
Graph Model	Object-Spatial Programming (OSP)

Project Structure
MindMate/
├── backend/
│   └── mindmate.jac       # Jaseci graph logic (nodes, edges, walkers)
├── frontend/
│   └── app.py             # Streamlit interface
├── README.md              # Documentation
└── requirements.txt       # Dependencies

How to Run the Project

Follow the steps below to run MindMate Harmony Space locally.

1. Install Prerequisites

You must have Python 3.8+ installed.

Install required libraries:

pip install jaseci streamlit

2. Run the Backend (Jaseci Brain)
Step 1 — Start the Jaseci Shell
jsctl -m


(If warnings appear, ignore them. Wait for the jaseci > prompt.)

Step 2 — Register Backend Code

Inside the shell:

sentinel register -name mindmate backend/mindmate.jac

Step 3 — Test Backend Logic
A. Log a Mood Entry
walker run log_mood -ctx '{"mood_score": 8, "description": "Feeling great", "triggers_list": ["Coding"]}'

B. Get Therapist Advice
walker run get_therapist_advice

3. Run the Frontend (Streamlit UI)

Open a new terminal window (keep Jaseci shell running).

Navigate to your project folder:

cd MindMate


Run the Streamlit app:

streamlit run frontend/app.py


Your browser will open the UI automatically (usually at http://localhost:8501).

🏆 Hackathon Implementation Details
Object-Spatial Graph (OSP)

Graph models emotions using emotion_entry nodes

Triggers stored in trigger nodes

Relationships linked via triggered_by edges

Multi-Agent AI Architecture

log_mood → Input agent

get_therapist_advice → Analysis agent

Jac Client + UI Visualization

Streamlit displays mood logs

Visualizes trigger patterns

Demonstrates emotional graph connections

Demo-Ready Setup

Frontend runs in a polished presentation mode
Backend terminal displays real OSP execution

Purpose

MindMate Harmony Space offers a safe, supportive, and intelligent mental-wellbeing companion—helping users understand themselves better through data-driven emotional insight.