import json
from datetime import datetime

# Predefined motivational tips based on mood
motivation_tips = {
    "Happy": "Great energy! Let's tackle the tough topics today.",
    "Neutral": "Steady progress is good progress. Keep going!",
    "Tired": "You're doing great — even small steps count on low-energy days!",
    "Stressed": "Take deep breaths. You're capable of overcoming this!"
}

# Function to create study plan based on mood
def create_study_plan(subjects, hours_per_day, mood):
    plan = []
    hours = int(hours_per_day)
    subjects_list = [s.strip() for s in subjects.split(",")]
    num_subjects = len(subjects_list)

    if mood == "Happy":
        for i in range(hours):
            plan.append(f"{i+1} hr: Tackle a new topic in {subjects_list[i % num_subjects]}")
    elif mood == "Neutral":
        for i in range(hours):
            plan.append(f"{i+1} hr: Continue with current topic in {subjects_list[i % num_subjects]}")
    elif mood == "Tired":
        for i in range(hours - 1):
            plan.append(f"{i+1} hr: Easy topic in {subjects_list[i % num_subjects]} (Revision)")
        plan.append(f"{hours} hr: Rest or Watch educational video")
    elif mood == "Stressed":
        for i in range(hours - 2):
            plan.append(f"{i+1} hr: Light reading or concept review in {subjects_list[i % num_subjects]}")
        plan += [f"{hours-1} hr: Meditation/Walk", f"{hours} hr: Educational podcast or light video"]

    return plan

# Function to handle journaling
def save_journal(entry):
    today = datetime.now().strftime("%Y-%m-%d")
    with open("journal_entries.json", "a") as file:
        file.write(json.dumps({today: entry}) + "\n")
    print("✅ Entry saved. See you tomorrow, champ!")

# Main Program
def run_studybuddy():
    print("🎓 Welcome to StudyBuddy GPT!\n")

    subjects = input("📘 What are your subjects?\n> ")
    hours_per_day = input("\n⏱ How many hours can you study per day?\n> ")

    while True:
        mood = input("\n🧠 How are you feeling today? (Happy / Neutral / Tired / Stressed)\n> ").capitalize()
        if mood not in ["Happy", "Neutral", "Tired", "Stressed"]:
            print("❌ Invalid mood. Please try again.")
            continue

        print("\n🗓 Here's your study plan for today:")
        plan = create_study_plan(subjects, hours_per_day, mood)
        for task in plan:
            print("- " + task)

        print("\n💡 Tip:", motivation_tips[mood])

        action = input("\nWould you like to journal or continue? (Journal / Continue / Exit)\n> ").capitalize()
        if action == "Journal":
            entry = input("📝 Write your journal entry:\n> ")
            save_journal(entry)
        elif action == "Exit":
            print("👋 Goodbye! Come back tomorrow for a new plan.")
            break

if __name__ == "__main__":
    run_studybuddy()
