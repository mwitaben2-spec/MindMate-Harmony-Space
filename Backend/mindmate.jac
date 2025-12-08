version: "1.0";

# 1. DEFINE NODES
node person {
    has name;
}

node emotion_entry {
    has mood_score;
    has description;
    has timestamp;
}

node trigger {
    has name;
}

node advice {
    has content;
}

# 2. DEFINE EDGES
edge felt_at;
edge triggered_by;
edge suggested;

# 3. WALKER: LOG MOOD
walker log_mood {
    has mood_score;
    has description;
    has triggers_list;

    root {
        # Create mood node
        mood_node = spawn node::emotion_entry;
        mood_node.mood_score = mood_score;
        mood_node.description = description;
        mood_node.timestamp = "2025-12-08";
        
        # Link and traverse
        here ++> mood_node;
        take mood_node;
    }

    emotion_entry {
        # Link triggers
        for t in triggers_list {
            t_node = spawn node::trigger;
            t_node.name = t;
            here +[triggered_by]+> t_node;
        }
        
        # --- SAFE REPORT BLOCK ---
        # We removed the ID check to prevent errors.
        # We only report variables we explicitly created.
        report {
            "status": "Mood logged successfully",
            "logged_desc": here.description
        };
    }
}

# 4. WALKER: THERAPIST
walker get_therapist_advice {
    root {
        # Go to the most recent mood
        take --> node::emotion_entry; 
    }

    emotion_entry {
        # Generate advice
        advice_text = "Based on your feeling of " + here.description + ", try deep breathing.";
        
        # Save advice to graph
        advice_node = spawn node::advice;
        advice_node.content = advice_text;
        here +[suggested]+> advice_node;

        report {
            "latest_mood": here.description,
            "therapist_advice": advice_text
        };
    }
}