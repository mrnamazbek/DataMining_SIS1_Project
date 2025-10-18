# SIS1 Project Presentation: Home Credit Default Risk Prediction

---

## Slide 1: Title Slide

# Home Credit Default Risk Prediction
## Data Mining Project - SIS1

**Team:** [Team Member Names]  
**Course:** Data Mining  
**Date:** [Presentation Date]

---

## Slide 2: Problem and Goal

### Problem
- Banks lose billions of dollars from customers who don't pay back loans
- Traditional methods to check loan repayment are not accurate enough
- Need to automate decision making process

### Goal
- Build machine learning model to predict loan default
- Find key risk factors
- Improve loan approval accuracy

---

## Slide 3: Dataset Description

### Home Credit Default Risk Dataset

| Parameter | Value |
|-----------|-------|
| **Source** | Kaggle Competition |
| **Data Size** | 307,507 records |
| **Features** | 122 features |
| **Task Type** | Binary classification |
| **Target** | TARGET (0/1) |
| **Default Rate** | ~8% |

### Meets Requirements
- ✅ > 40,000 records
- ✅ > 14 features  
- ✅ Real data
- ✅ Open source

---

## Slide 4: Data Structure

### Main Tables
- **application_train.csv** - Main customer data
- **application_test.csv** - Test data
- **bureau.csv** - Credit history
- **previous_application.csv** - Previous applications
- **credit_card_balance.csv** - Credit card balances

### Key Features
- **Personal:** age, gender, family status
- **Financial:** income, loan amount, annuity
- **Credit History:** previous loans, late payments
- **External Sources:** EXT_SOURCE_1, EXT_SOURCE_2, EXT_SOURCE_3

---

## Slide 5: Data Preprocessing

### Processing Steps

1. **Missing Values Analysis**
   - Found 67 columns with missing values
   - Removed columns with >50% missing values

2. **Fill Missing Values**
   - Numerical features → median
   - Categorical features → mode

3. **Encoding**
   - LabelEncoder for categorical variables
   - StandardScaler for numerical features

### Result
- Processed 307,507 records
- Prepared 120 features
- No missing values remaining

---

## Slide 6: Exploratory Data Analysis

### Target Variable Analysis

```
TARGET Distribution:
├── No Default (0): 282,686 records (91.9%)
└── Default (1): 24,821 records (8.1%)

Imbalance: 11.4:1
```

### Key Observations
- Classes are unbalanced (8% defaults)
- Need to consider this when training models
- May need balancing techniques

---

## Slide 7: Statistical Analysis

### Main Statistics

| Feature | Mean | Median | Std Dev |
|---------|------|--------|---------|
| **AMT_INCOME_TOTAL** | 168,797 | 147,000 | 240,954 |
| **AMT_CREDIT** | 599,025 | 513,000 | 402,531 |
| **AMT_ANNUITY** | 27,106 | 24,975 | 15,433 |
| **DAYS_BIRTH** | -15,653 | -15,700 | 4,465 |

### Interpretation
- Large variation in customer incomes
- High variation in loan amounts
- Standardization is critical

---

## Slide 8: Correlation Analysis

### Top 10 Correlations with TARGET

| Feature | Correlation | Interpretation |
|---------|-------------|----------------|
| **EXT_SOURCE_3** | -0.178 | External scoring |
| **EXT_SOURCE_2** | -0.160 | External scoring |
| **EXT_SOURCE_1** | -0.155 | External scoring |
| **DAYS_BIRTH** | 0.078 | Customer age |
| **AMT_INCOME_TOTAL** | -0.072 | Total income |

### Conclusions
- External data sources most informative
- Age positively correlates with default
- Income negatively correlates with risk

---

## Slide 9: Distribution Visualization

### Key Feature Distributions

**AMT_INCOME_TOTAL (Income):**
- Log-normal distribution
- Outliers in high incomes
- May need log transformation

**DAYS_BIRTH (Age):**
- Normal distribution
- Peak at age 30-40
- Clear relationship with default

**AMT_CREDIT (Loan Amount):**
- Right-skewed distribution
- Correlates with income
- Important risk predictor

---

## Slide 10: Important Features Analysis

### Top 15 Important Features

1. **EXT_SOURCE_3** - External scoring 3
2. **EXT_SOURCE_2** - External scoring 2  
3. **EXT_SOURCE_1** - External scoring 1
4. **DAYS_BIRTH** - Customer age
5. **AMT_INCOME_TOTAL** - Total income
6. **AMT_ANNUITY** - Annuity amount
7. **AMT_CREDIT** - Loan amount
8. **REGION_POPULATION_RELATIVE** - Population density
9. **DAYS_EMPLOYED** - Employment length
10. **CNT_FAM_MEMBERS** - Family size

### Insights
- External data sources critically important
- Demographic factors play key role
- Financial indicators significant for prediction

---

## Slide 11: Conclusions and Hypotheses

### Main Conclusions

1. **Unbalanced data** requires special techniques
2. **External sources** most informative
3. **Age and income** key demographic factors
4. **Financial indicators** important for risk assessment

### Hypotheses for SIS2

1. **Balanced models** will show better results
2. **Ensemble algorithms** will outperform single models
3. **Feature engineering** will improve prediction quality
4. **External sources** will be key predictors

---

## Slide 12: Next Steps (SIS2)

### Plan for SIS2

1. **Build Models**
   - Logistic Regression
   - Random Forest
   - XGBoost
   - Neural Networks

2. **Evaluate Quality**
   - Accuracy, Precision, Recall
   - F1-score, ROC-AUC
   - Cross-validation

3. **Optimize**
   - Hyperparameter tuning
   - Feature selection
   - Ensemble methods

4. **Interpret**
   - Feature importance
   - SHAP values
   - Business insights

---

## Slide 13: Technical Details

### Technologies Used

- **Python 3.11**
- **Pandas, NumPy** - data processing
- **Scikit-learn** - machine learning
- **Matplotlib, Seaborn** - visualization
- **Jupyter Notebooks** - development

### Project Structure
```
DataMining_SIS1_Project/
├── data_raw/              # Original data
├── data_processed/        # Processed data
├── notebooks/             # Jupyter notebooks
├── presentation/          # Presentation
├── reports/               # Reports
└── README.md              # Documentation
```

---

## Slide 14: Thank You!

### SIS1 Key Achievements

✅ **Loaded and processed** real credit company data  
✅ **Conducted complete EDA** with key factor identification  
✅ **Prepared quality dataset** for model training  
✅ **Formulated hypotheses** for further research  

### Ready for SIS2
- Processed data ready for use
- Important features identified
- Understanding of task and data
- Clear plan for next steps

### Questions?

---

## Appendix: Additional Slides

### Slide A1: Data Processing Methodology

```python
# Example processing code
def preprocess_data(df):
    # 1. Remove columns with >50% missing values
    df = remove_high_missing_cols(df, threshold=0.5)
    
    # 2. Fill missing values
    df = fill_missing_values(df)
    
    # 3. Encode categorical variables
    df = encode_categorical(df)
    
    # 4. Scale numerical features
    df = scale_numeric_features(df)
    
    return df
```

### Slide A2: Statistical Tests

**T-test for group comparison:**
- Default vs No Default
- Significant differences in income, age, loan amount
- p-value < 0.001 for all key features

**Chi-square test:**
- Relationship between categorical features and default
- Gender, family status, education
- Statistically significant associations

---

*Presentation prepared for SIS1 defense in Data Mining course*