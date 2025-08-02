# Project Title  
StudySync – Mood-Based AI Study Planner

## Abstract  
StudySync is a mood-adaptive AI-powered study planner built using Python and Streamlit. It personalizes your daily study schedule based on your current emotional state. By recognizing that productivity depends on mood, it tailors study plans with smart workload distribution — focusing on intensive topics on high-energy days and light revision or reflection when the user is tired or stressed. It also includes journaling features and motivational messages, helping students stay consistent, self-aware, and encouraged through ups and downs in their learning journey.

## Program  
The project is structured in Streamlit with the following key components:

1. Collecting User Input  
```python
st.title("StudySync – Your Mood-Based Study Planner")
name = st.text_input("Enter your name:")
subjects = st.text_area("List your subjects (comma-separated):").split(",")
study_hours = st.slider("How many hours do you want to study today?", 1, 12, 4)
```

2. Mood Detection  
```python
mood = st.radio("How are you feeling today?", ["Happy", "Neutral", "Tired", "Stressed"])
```

3. Study Plan Generator  
```python
def generate_plan(subjects, hours, mood):
    plan = []
    for i in range(hours):
        subject = subjects[i % len(subjects)].strip()
        if mood == "Happy":
            plan.append(f"{i+1} hr: Learn a new topic in {subject}")
        elif mood == "Neutral":
            plan.append(f"{i+1} hr: Regular study for {subject}")
        elif mood == "Tired":
            plan.append(f"{i+1} hr: Light revision of {subject}")
        elif mood == "Stressed":
            plan.append(f"{i+1} hr: Relax with {subject} flashcards")
    return plan
```

4. Motivational Tips  
```python
motivation = {
    "Happy": "Keep going strong — you're on fire today!",
    "Neutral": "Consistency is key — you're doing great!",
    "Tired": "Even small efforts matter. Be kind to yourself.",
    "Stressed": "Take it easy. You're allowed to pause and breathe."
}
```

5. Journaling and Journal View  
```python
entry = st.text_area("Write your journal entry for today:")
if st.button("Save Entry"):
    with open("journal.txt", "a") as f:
        f.write(f"{datetime.now().date()} - {mood} - {entry}\n")
    st.success("Journal entry saved!")

if st.checkbox("View Past Journal Entries"):
    with open("journal.txt", "r") as f:
        st.text(f.read())
```

## Output (Sample)  
🎯 Study Plan for Today (Mood: Stressed)  
1 hr: Relax with Math flashcards  
1 hr: Light revision of Physics  
1 hr: Watch a science YouTube explainer  
1 hr: Breathing break + revise Biology formulas

💡 Tip: Take it easy. You're allowed to pause and breathe.

📝 Journal:  
Today I felt anxious but still got some studying done. I’ll take tomorrow slow.

## Screenshots:

<img width="1918" height="905" alt="image" src="https://github.com/user-attachments/assets/fd59fda0-aaf0-4ed2-aa51-b79af48c15b3" />

<img width="1919" height="900" alt="image" src="https://github.com/user-attachments/assets/7edb4336-9b36-41aa-943f-21f7c9fb5319" />

<img width="1917" height="902" alt="image" src="https://github.com/user-attachments/assets/702ac5ec-80a7-4b77-8184-05c17845af83" />

<img width="1916" height="900" alt="image" src="https://github.com/user-attachments/assets/cb34ccf6-2d1a-483d-bf07-39701e69f777" />

## Demo Link:
https://studysyncyouragent.streamlit.app/
