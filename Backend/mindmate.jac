version: "1.0";

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

edge felt_at;
edge triggered_by;
edge suggested;

walker log_mood {
    has mood_score;
    has description;
    has triggers_list;

    root {
        mood_node = spawn node::emotion_entry;
        mood_node.mood_score = mood_score;
        mood_node.description = description;
        mood_node.timestamp = "2025-12-08";
        
        here ++> mood_node;
        take mood_node;
    }

    emotion_entry {
        for t in triggers_list {
            t_node = spawn node::trigger;
            t_node.name = t;
            here +[triggered_by]+> t_node;
        }
        
        report {
            "status": "Mood logged successfully",
            "logged_desc": here.description
        };
    }
}

walker get_therapist_advice {
    root {
        take --> node::emotion_entry; 
    }

    emotion_entry {
        advice_text = "Based on your feeling of " + here.description + ", try deep breathing.";
        
        advice_node = spawn node::advice;
        advice_node.content = advice_text;
        here +[suggested]+> advice_node;

        report {
            "latest_mood": here.description,
            "therapist_advice": advice_text
        };
    }
}