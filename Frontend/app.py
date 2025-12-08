import streamlit as st
import json
# In a real scenario, you import the Jaseci JSORC or client. 
# For this hackathon structure, we will simulate the 'Spawn' call 
# behavior to demonstrate how the client code SHOULD look.

st.set_page_config(page_title="MindMate Harmony", layout="wide")

st.title("🧠 MindMate Harmony Space")
st.markdown("### AI Mental-Wellbeing Companion")

# Sidebar for controls
st.sidebar.header("User Profile")
user_name = st.sidebar.text_input("Name", "Guest")

# --- SECTION 1: MOOD LOGGING [cite: 134] ---
st.header("1. How are you feeling?")
col1, col2 = st.columns(2)

with col1:
    mood_val = st.slider("Mood Score (1-10)", 1, 10, 5)
    mood_desc = st.text_area("Describe your feelings...", "I feel anxious about the hackathon deadline.")

with col2:
    triggers = st.multiselect(
        "Select Triggers [cite: 126]",
        ["Work", "Sleep", "Social", "Finance", "Health", "Weather"],
        ["Work"]
    )

if st.button("Log Mood"):
    # This block demonstrates calling the Walker (Agent) defined in backend
    # EQUIVALENT TO: spawn(walker='log_mood', args={...}) [cite: 136]
    
    payload = {
        "name": "log_mood",
        "args": {
            "mood_score": mood_val,
            "description": mood_desc,
            "triggers_list": triggers
        }
    }
    
    # Simulate a successful backend response for the demo
    st.success(f"Mood Logged! Created Graph Nodes: Emotion({mood_val}) -> Triggers({triggers})")
    st.json(payload) # Showing the data structure for judges

# --- SECTION 2: AI THERAPIST (byLLM)  ---
st.markdown("---")
st.header("2. AI Therapist Insights")

if st.button("Get Coping Strategy"):
    # EQUIVALENT TO: spawn(walker='get_therapist_advice')
    
    st.info("Consulting 'byLLM' agent on the backend...")
    
    # Mock response based on the logic in mindmate.jac
    response = {
        "latest_mood": mood_desc,
        "therapist_advice": f"I notice you are feeling: '{mood_desc}'. considering this is triggered by {triggers}, I suggest taking a 5-minute break to practice mindfulness. Break the task down into smaller steps."
    }
    
    st.chat_message("assistant").write(response['therapist_advice'])

# --- SECTION 3: VISUALIZATION (OSP Graph)  ---
st.markdown("---")
st.header("3. Your Emotional Graph")
st.caption("Visualizing the OSP (Object Spatial Profile)")

# Simple visualization of the graph structure you are building
st.graphviz_chart(f"""
    digraph {{
        rankdir=LR;
        User -> "Mood: {mood_val}/10" [label="felt_at"];
        "Mood: {mood_val}/10" -> "{triggers[0] if triggers else 'Unknown'}" [label="triggered_by"];
        "Mood: {mood_val}/10" -> "Advice Node" [label="suggested"];
    }}
""")