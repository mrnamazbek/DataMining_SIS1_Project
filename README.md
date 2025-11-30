# Data Mining Project - Home Credit Default Risk Prediction

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=36BCF7&lines=Credit+Risk+Prediction;Machine+Learning;Data+Mining;Financial+Analytics)](https://git.io/typing-svg)

---

## Project Overview  
This project is part of the **Data Mining course @ KBTU (MSc Program)**.  
We analyze the **Home Credit Default Risk** dataset from Kaggle and build models to predict if customers will pay back their loans.  

**Dataset:** [Home Credit Default Risk](https://www.kaggle.com/competitions/home-credit-default-risk)  

### Why this dataset?  
- **Open and reliable** → Official Kaggle competition dataset  
- **Size** → More than **300,000+ records**  
- **Rich data** → More than **120 features** including personal, financial and behavioral data  
- **Real importance** → Predicting loan default risk is one of the most important problems in banking and fintech

---

## Project Requirements  

- More than **14 features** ✅  
- More than **40,000 records** ✅  
- Open dataset ✅  
- Group project (max 3 students) ✅  

---

## Project Deliverables  

### Part 1 – SIS 1 ✅ COMPLETED

1. **Project Proposal** ✅  
   - Problem statement and objectives  
   - Research questions and hypotheses  
   - Dataset choice justification  

2. **Data Work** ✅  
   - Data collection (from Kaggle)  
   - Dataset description (size, features, type, source)  
   - Data cleaning (missing values, outliers, inconsistencies)  
   - Data transformation (scaling, encoding, feature selection)  

3. **Exploratory Data Analysis (EDA)** ✅  
   - Summary statistics (mean, variance, distribution)  
   - Correlations between variables  
   - Visualizations (histograms, scatter plots, heatmaps)  
   - Initial insights  

4. **Presentation** ✅  
   - Problem statement  
   - Dataset  
   - Preprocessing steps  
   - EDA results  

---

### Part 2 – SIS 2 🔄 PLANNED

1. **Data Mining Techniques**  
   - Apply **4–5 algorithms** (classification/regression)  
   - Justify algorithm selection  

2. **Model Evaluation & Comparison**  
   - Metrics: Accuracy, Precision/Recall, RMSE, AUC  
   - Cross-validation or train-test split  
   - Compare performance  

3. **Results & Interpretation**  
   - Confusion matrix, ROC curve, feature importance  
   - Highlight key insights  
   - Discuss real-world meaning of results  

4. **Presentation**  
   - Introduction & background  
   - Dataset & preprocessing (recap)  
   - Methodology (algorithms)  
   - Results & evaluation

---

## Tech Stack  

### Languages  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge&logo=postgresql&logoColor=white)  

### Machine Learning & AI  
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-2F7BBF?style=for-the-badge&logo=scikitlearn&logoColor=white)  
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)  
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)  
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)  

### Big Data & Orchestration  
![Apache Spark](https://img.shields.io/badge/Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)  
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)  

### Databases  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)  
![Oracle](https://img.shields.io/badge/Oracle_SQL-F80000?style=for-the-badge&logo=oracle&logoColor=white)  

---

## Project Structure  

```
DataMining_SIS1_Project/
├── data_raw/                    # Original data (CSV files)
│   ├── application_train.csv    # Main training data
│   ├── application_test.csv     # Test data
│   ├── bureau.csv              # Credit history
│   └── ...
├── data_processed/              # Processed data
│   ├── train_processed.csv      # Processed training data
│   ├── test_processed.csv       # Processed test data
│   └── feature_info.json       # Feature information
├── notebooks/                    # Jupyter notebooks
│   ├── 01_data_preprocessing.ipynb  # Data preprocessing
│   └── 02_eda.ipynb            # Exploratory Data Analysis
├── presentation/                 # Presentation slides
│   └── sis1_presentation.md     # Presentation slides
├── reports/                      # Reports and documentation
│   └── project_proposal.md      # Project Proposal
├── scripts/                      # Helper Python scripts
├── models/                       # Saved models (SIS2)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## Project Roadmap  

### ✅ SIS 1 - COMPLETED
1. **Dataset download & setup** ✅  
2. **Data cleaning** (missing values, outliers) ✅  
3. **Feature engineering** (scaling, encoding, transformations) ✅  
4. **Exploratory Data Analysis (EDA)** with visualizations ✅  
5. **Presentation preparation** ✅  

### 🔄 SIS 2 - PLANNED
6. **Modeling** with multiple algorithms  
7. **Evaluation** (metrics, comparison)  
8. **Interpretation & presentation**  

---

## Key SIS1 Results  

### 📈 **Dataset Statistics**
- **307,507 records** of customers
- **122 features** (personal, financial, credit)
- **8.1% defaults** (unbalanced data)
- **0 missing values** after processing

### 🔍 **Key Insights**
- **External data sources** (EXT_SOURCE_1,2,3) most informative
- **Customer age** positively correlates with default
- **Income** negatively correlates with risk
- **Financial indicators** critically important for prediction

### 🛠️ **Technical Achievements**
- Complete automation of data preprocessing
- Comprehensive EDA with visualizations
- Ready pipeline for model training
- Quality documentation and presentation

---

## Team & Contacts  

👨‍💻 **Namazbek Bekzhanov** — MSc @ KBTU  
📧 [namazbekzhan@gmail.com](mailto:namazbekzhan@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/namazbek-bekzhanov/)  

---

⚙️ *Turning raw data into real insights — the essence of Data Mining.*