import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# PART 1: LOAD DATASET



data = pd.DataFrame({
    'hours_studied': [2, 4, 6, 8, 5, 7, 3, 9, 1, 6],
    'sleep_hours': [5, 6, 7, 8, 6, 7, 5, 8, 4, 7],
    'distractions': [3, 2, 1, 1, 2, 1, 4, 1, 5, 2],
    'attendance': [60, 70, 80, 90, 75, 85, 65, 95, 50, 78],
    'score': [50, 60, 75, 90, 70, 85, 55, 92, 40, 78]
})

# Features & Target
X = data[['hours_studied', 'sleep_hours', 'distractions', 'attendance']]
y = data['score']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

print("✅ Model trained successfully")


# PART 2: USER INPUT


print("\n--- Enter Your Details ---")

hours = float(input("Study hours per day: "))
sleep = float(input("Sleep hours: "))
distractions = float(input("Distraction time (hrs): "))
attendance = float(input("Attendance %: "))

# Prediction
predicted_score = model.predict([[hours, sleep, distractions, attendance]])
predicted_score = predicted_score[0]

print(f"\n🎯 Predicted Exam Score: {round(predicted_score, 2)}")


# PART 3: TO-DO PRIORITIZER


print("\n--- Enter Your Tasks ---")

tasks = []
n = int(input("How many tasks? "))

for i in range(n):
    print(f"\nTask {i+1}")
    name = input("Task name: ")
    deadline = int(input("Days left: "))
    difficulty = int(input("Difficulty (1-5): "))
    importance = int(input("Importance (1-5): "))

    priority = (importance * 2 + difficulty) / deadline

    tasks.append({
        "name": name,
        "priority": priority
    })

# Sort tasks
tasks = sorted(tasks, key=lambda x: x['priority'], reverse=True)

print("\n📋 Task Priority List:")
for t in tasks:
    print(f"{t['name']} -> Priority Score: {round(t['priority'],2)}")


# PART 4: SMART SUGGESTION


print("\n--- AI Suggestion ---")

if predicted_score < 60:
    print("⚠️ Focus on studying first. You're falling behind.")
elif predicted_score < 80:
    print("📚 Balance study and tasks.")
else:
    print("🔥 You're doing great. Maintain consistency.")
