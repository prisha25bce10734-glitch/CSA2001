# 📚 AI Study Planner

## 📌 Overview

The AI Study Planner is a simple machine learning-based project that helps students manage their studies more effectively. It predicts a student's exam score based on study habits and prioritizes daily tasks using a smart scoring system.

This project combines **machine learning** and **decision-making logic** to solve a real-world problem faced by students.

---

## 🚀 Features

* 🎯 Predicts exam score using study-related inputs
* 📋 Prioritizes tasks based on urgency and importance
* 🧠 Combines AI prediction with logical decision-making
* 💻 Simple command-line interface

---

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

---

## 📂 Project Structure

```
AI-Study-Planner/
│
├── dataset/
│   └── student_data.csv
│
├── src/
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
https://github.com/prisha25bce10734-glitch/CSA2001
```

2. Navigate to the project folder:

```
https://github.com/prisha25bce10734-glitch/CSA2001/tree/main/project-code
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the main Python file:

```
python src/main.py
```

---

## 📊 Input Parameters

### For Score Prediction:

* Study hours per day
* Sleep hours
* Distraction time (in hours)
* Attendance percentage

### For Task Prioritization:

* Task name
* Deadline (in days)
* Difficulty (1–5)
* Importance (1–5)

---

## 🧮 Task Prioritization Formula

Priority is calculated using:

Priority = (Importance × 2 + Difficulty) / Deadline

Tasks with higher priority values are completed first.

---

## 📈 Output

* 🎯 Predicted exam score
* 📋 Sorted list of tasks based on priority
* 💡 Basic suggestion based on performance

---

## ⚠️ Limitations

* Uses a small dataset, so predictions may not be highly accurate
* Assumes linear relationship between inputs and score
* Does not include real-time data tracking

---

## 🔮 Future Improvements

* Use a larger and real-world dataset
* Improve accuracy with advanced models (Random Forest, etc.)
* Add graphical user interface (Streamlit)
* Implement notifications and reminders
* Convert into a web or mobile application

---

## 📚 Learning Outcomes

* Understanding of basic machine learning concepts
* Working with datasets using Pandas
* Model training and prediction using Scikit-learn
* Applying logic for real-world problem solving
* Structuring and documenting a project

---



