# Project Proposal: Home Credit Default Risk Prediction

---

## Problem Statement

**Problem:** Banks lose billions of dollars each year because some customers don't pay back their loans. Traditional methods to check if someone can pay back a loan are not always accurate.

**Goal:** Build a machine learning model to predict if a customer will default on their loan based on their personal and financial information.

## Objectives

### Main Goals:
1. **Build a classification model** to predict loan default (TARGET = 1)
2. **Find key risk factors** that affect loan repayment
3. **Analyze data** including cleaning, EDA and visualization
4. **Prepare quality dataset** for machine learning models

### Success Metrics:
- Model accuracy > 80%
- AUC-ROC > 0.75
- Find at least 5 key risk factors

## Research Questions

1. **What personal factors** most affect loan default risk?
2. **How do age and family status** relate to loan risk?
3. **Does income and education** affect loan repayment?
4. **Can we improve model accuracy** with better data processing?
5. **Which external data sources** are most useful for prediction?

## Dataset Justification

### Why Home Credit Default Risk?

**Meets Requirements:**
- **Data size:** > 300,000 records (307,507 rows in train)
- **Number of features:** 122 features (> 14 required)
- **Real data:** Data from actual credit company
- **Open source:** Kaggle Competition

**Practical Value:**
- Solves real business problem
- Can be used in real banking
- High commercial value

**Technical Challenge:**
- Mixed data types (numbers, categories)
- Missing values need handling
- Unbalanced classes (default ~8%)
- Multiple data sources

## Expected Outcomes

### SIS1 (Current Phase):
- Clean and prepared dataset
- Complete EDA with visualizations
- Found correlations and patterns
- Ready for model building

### SIS2 (Next Phase):
- Trained machine learning models
- Algorithm comparison by metrics
- Feature importance interpretation
- Business recommendations

## Methodology

### Phase 1: Data Preprocessing
- Load and combine data from all sources
- Handle missing values
- Encode categorical variables
- Scale numerical features

### Phase 2: Exploratory Data Analysis
- Statistical analysis of distributions
- Correlation analysis
- Data visualization
- Find outliers and anomalies

### Phase 3: Feature Engineering
- Create new features
- Select most informative features
- Handle time series data

## Project Structure

```
DataMining_SIS1_Project/
├── data_raw/              # Original data (CSV files)
├── data_processed/        # Cleaned data
├── notebooks/             # Jupyter notebooks
│   ├── 01_data_preprocessing.ipynb
│   └── 02_eda.ipynb
├── presentation/          # Presentation slides
├── scripts/               # Helper Python files
├── reports/               # Reports and documentation
├── models/                # Saved models (SIS2)
└── README.md              # Project description
```

## Timeline

- **Week 1:** Data Preprocessing and cleaning
- **Week 2:** Exploratory Data Analysis and visualization
- **Week 3:** Prepare presentation and defend SIS1
- **Week 4-6:** SIS2 - Build and compare models

## Team Roles

| Member | Responsibility |
|--------|----------------|
| **Namazbek** | Data loading, cleaning and preprocessing |
| **Shyntas** | EDA, visualizations, correlation analysis |
| **Ibragim** | Presentation, results formatting |

---

*This project is part of the Data Mining course and aims to apply data analysis methods to solve real business problems.*
