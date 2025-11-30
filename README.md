# 🏠 Home Credit Default Risk Prediction 💰

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 👋 What is this project?
Imagine you are a bank. A person comes to you and asks for money (a loan). 
**How do you know if they will pay it back?** 🤔

This project uses **Data Mining** (computer magic 🪄) to look at information about people and predict:
*   ✅ **0**: They will pay it back (Good).
*   ❌ **1**: They will have trouble paying (Risky).

We want to help the bank say "Yes" to the right people!

---

## 🗺️ How It Works (Visual Flow)

Here is the path we took to solve this problem:

```mermaid
graph LR
    A[📂 Raw Data] -->|Cleaning & Fixing| B[🧹 Preprocessing]
    B -->|Selecting Best Info| C[📊 Feature Selection]
    C -->|Teaching the Computer| D[🤖 Modeling]
    D -->|Checking Answers| E[🏆 Evaluation]
    E -->|Final Result| F[🚀 Best Model]
```

---

## 📂 Project Structure

Here is what is inside our folders:

```text
📦 DataMining_SIS1_Project
 ┣ 📂 notebooks          # 📓 Where the code lives
 ┃ ┣ 📜 01_data_preprocessing.ipynb  # Cleaning the messy data
 ┃ ┣ 📜 02_eda.ipynb                 # Looking at pictures of data
 ┃ ┗ 📜 03_modeling.ipynb            # The AI models (SIS 2)
 ┣ 📂 presentation       # 🎤 Slides for our talk
 ┃ ┣ 📜 presentation.md              # The slides text
 ┃ ┗ 📜 explanation.md               # Detailed explanation
 ┣ 📂 reports            # 📄 Documents
 ┃ ┗ 📜 project_proposal.md          # Our initial plan
 ┣ 📜 requirements.txt   # 🛠️ List of tools we used
 ┗ 📜 README.md          # 📖 You are reading this!
```

---

## 🧩 Project Parts

### Part 1: SIS 1 (Preparation) 🛠️
*   We found a big dataset (Home Credit).
*   We cleaned it (fixed missing numbers).
*   We chose the **42 most important things** (features) to look at, like:
    *   🎂 Age (`DAYS_BIRTH`)
    *   💼 Job (`DAYS_EMPLOYED`)
    *   💵 Credit Amount (`AMT_CREDIT`)
    *   📈 External Scores (`EXT_SOURCE`)

### Part 2: SIS 2 (The AI Models) 🤖
We tested **5 different brains** (algorithms) to see which one is smartest:

1.  **Logistic Regression** (Simple & Fast) 🏃
2.  **Decision Tree** (Like a flowchart) 🌳
3.  **Random Forest** (Many trees voting) 🌲🌲🌲
4.  **Gradient Boosting** (Learning from mistakes) 🚀 **(WINNER!)**
5.  **Naive Bayes** (Based on probability) 🎲

---

## 🏆 Results: Which Model is Best?

We want the model with the highest **ROC AUC** score (a score from 0 to 1).
*   0.5 = Guessing randomly 🤷
*   1.0 = Perfect prediction 🎯

| Model Name | Score (ROC AUC) | Verdict |
| :--- | :---: | :--- |
| **Gradient Boosting** | **0.75** | 🥇 **Best!** |
| **Random Forest** | **0.74** | 🥈 Very Good |
| Logistic Regression | 0.72 | 🥉 Okay |
| Naive Bayes | 0.65 | Weak |
| Decision Tree | 0.54 | Bad |

---

## 🚀 How to Run This

1.  **Download** this repository.
2.  **Install** the tools:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Open** the notebooks:
    ```bash
    jupyter notebook
    ```
4.  **Run** `notebooks/03_modeling.ipynb` to see the magic happen! ✨

---

## 👥 Team
*   **Student 1**: Namazbek
*   **Student 2**: [Name]
*   **Student 3**: [Name]

---
*Made with ❤️ for Data Mining Course*