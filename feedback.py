# feedback.py

def store_feedback(username, feedback):
    with open("feedback_sample.txt", "a") as f:
        f.write(f"{username}: {feedback}\n")

