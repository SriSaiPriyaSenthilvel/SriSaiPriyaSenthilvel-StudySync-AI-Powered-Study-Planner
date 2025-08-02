import streamlit as st
from datetime import datetime
import json

st.set_page_config(page_title="StudySync", page_icon="📘")

st.title("🎓 StudySync – AI-Powered Study Planner")
st.write("Mood-Adaptive AI Study Coach")

# User inputs
subjects = st.text_input("📘 Enter your subjects (comma-separated):", "Math, Physics, Biology")
hours = st.slider("⏱ How many hours can you study per day?", 1, 10, 4)
mood = st.selectbox("🧠 How are you feeling today?", ["Happy", "Neutral", "Tired", "Stressed"])

# Motivation tips
motivation_tips = {
    "Happy": "Great energy! Let's tackle the tough topics today.",
    "Neutral": "Steady progress is good progress. Keep going!",
    "Tired": "You're doing great — even small steps count on low-energy days!",
    "Stressed": "Take deep breaths. You're capable of overcoming this!"
}

# Function to generate study plan
def generate_plan(subjects, hours, mood):
    plan = []
    sub_list = [s.strip() for s in subjects.split(",")]
    num_subjects = len(sub_list)

    if mood == "Happy":
        for i in range(hours):
            plan.append(f"{i+1} hr: Tackle a new topic in {sub_list[i % num_subjects]}")
    elif mood == "Neutral":
        for i in range(hours):
            plan.append(f"{i+1} hr: Continue with current topic in {sub_list[i % num_subjects]}")
    elif mood == "Tired":
        for i in range(hours - 1):
            plan.append(f"{i+1} hr: Easy topic in {sub_list[i % num_subjects]} (Revision)")
        plan.append(f"{hours} hr: Rest or Watch educational video")
    elif mood == "Stressed":
        for i in range(hours - 2):
            plan.append(f"{i+1} hr: Light review in {sub_list[i % num_subjects]}")
        plan += [f"{hours-1} hr: Meditation/Walk", f"{hours} hr: Educational podcast"]

    return plan

# Study plan display
if st.button("Generate My Study Plan"):
    st.subheader("🗓 Your Personalized Study Plan")
    for task in generate_plan(subjects, hours, mood):
        st.markdown(f"- {task}")

    st.success("💡 " + motivation_tips[mood])

# Journal section
with st.expander("📝 Want to journal your thoughts today?"):
    journal_text = st.text_area("Write your journal entry:")
    if st.button("Save Journal"):
        today = datetime.now().strftime("%Y-%m-%d")
        try:
            with open("journal_entries_streamlit.json", "a") as file:
                file.write(json.dumps({today: journal_text}) + "\n")
            st.success("✅ Journal saved!")
        except Exception as e:
            st.error("❌ Error saving journal: " + str(e))

# Journal viewer section
with st.expander("📖 View Past Journal Entries"):
    try:
        with open("journal_entries_streamlit.json", "r") as file:
            for line in file:
                entry = json.loads(line)
                for date, text in entry.items():
                    st.markdown(f"**🗓 {date}**")
                    st.markdown(f"> {text}")
                    st.markdown("---")
    except FileNotFoundError:
        st.info("No journal entries yet.")
