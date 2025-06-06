
# ⚽ UEFA Champions League 2023–2024 Data Analysis Tool

## 📌 Overview

This Python-based console application allows users to search, filter, compare, and analyze UEFA Champions League 2023–2024 data. Designed as part of a university project, the tool demonstrates core skills in data structures, algorithms, and Python programming.

---

## 📊 Features

- 📁 Load data from CSV files (Kaggle-sourced Champions League dataset)
- 🔍 Search options:
  - By Squad (team name)
  - By Country
  - By Top Team Scorer
  - By Goal Difference (GD)
- 🗂 Sort and filter data by user-selected criteria
- 🧠 Compare teams or players by ranking in a specific column (e.g., Wins, Goals)
- 💾 Save results to:
  - `comparison_results.csv`
  - `sorted_results.csv`
  - `teams_in_<country>.csv`

---

## 🛠 Technologies Used

- Python 3.x
- pandas
- os (standard library)
- CSV file handling
- Encoding: `ISO-8859-1`

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/uefa-cl-2023-analysis.git
cd uefa-cl-2023-analysis
```

2. Ensure the Champions League CSV dataset is placed in the same folder as the script.

3. Run the script:
```bash
python main.py
```

---

## 🗃 Dataset

The dataset used in this project is sourced from Kaggle:
[UEFA Champions League 2023/2024 Dataset](https://www.kaggle.com/datasets/sharvagya/champions-league-2324)

---

## 📂 Folder Structure

```
uefa-cl-2023-analysis/
├── main.py
├── ChampionsLeague.csv
├── champs.csv
├── comparison_results.csv
├── sorted_results.csv
├── teams_in_es.csv
├── teams_in_fr.csv
├── README.md
```

---

## 👨‍🎓 Author

**Georgios Dionisopoulos**  
Supervisor: Mr. Gimeno Abraham  
Project for Advanced Data Structures and Algorithms Course

---

## 📄 License

This project is for academic and educational purposes. Attribution required.
