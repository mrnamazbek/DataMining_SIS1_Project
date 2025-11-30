# SIS1 Project Presentation: Home Credit Default Risk Prediction

---

## Slide 1: Title Slide

# 🏦 Home Credit Default Risk Prediction
## Data Mining Project - SIS1

**Team:** Namazbek, Shyntas, Ibragim  
**Course:** Data Mining  
**Date:** 21.10.25  

---

## Slide 2: Problem and Goal

### 🚨 The Problem
- Banks lose **billions of dollars** each year from bad loans
- Traditional credit checks are **not accurate enough**
- Need **better ways** to predict who will pay back loans

### 🎯 Our Goal
- Build **machine learning model** to predict loan defaults
- Find **key risk factors** that matter most
- Help banks make **better decisions**

---

## Slide 3: Dataset Description

### 📊 Home Credit Default Risk Dataset

| Parameter | Value |
|-----------|-------|
| **Source** | Kaggle Competition |
| **Data Size** | 307,507 records |
| **Original Features** | 122 features |
| **Selected Features** | 40 features |
| **Task Type** | Binary classification |
| **Target** | TARGET (0/1) |
| **Default Rate** | ~8% |

### ✅ Meets All Requirements
- ✅ **> 40,000 records** (307,507)
- ✅ **> 14 features** (40 selected)
- ✅ **Real data** from actual bank
- ✅ **Open source** dataset

---

## Slide 4: Data Structure

### 📁 Main Data Files
- **application_train.csv** - Main customer data (307,507 records)
- **application_test.csv** - Test data (48,746 records)
- **bureau.csv** - Credit history
- **previous_application.csv** - Previous applications
- **credit_card_balance.csv** - Credit card balances

### 🔍 Key Feature Categories
- **👤 Demographics:** age, gender, family size
- **💰 Financial:** income, loan amount, payments
- **📊 External Sources:** EXT_SOURCE_2, EXT_SOURCE_3
- **🏠 Housing:** owns car, owns house, housing type
- **💼 Employment:** job type, education, work experience

---

## Slide 5: Feature Selection Strategy

### 🎯 Why We Selected Only 40 Features?

**Original:** 122 features → **Selected:** 40 features (67% reduction)

### 📋 Feature Categories Selected:

| Category | Features | Examples |
|----------|----------|----------|
| **👤 Demographics** | 4 | Gender, Age, Children, Family Size |
| **💰 Financial** | 4 | Income, Credit Amount, Payments |
| **📊 External Sources** | 2 | EXT_SOURCE_2, EXT_SOURCE_3 |
| **💼 Employment** | 4 | Job Type, Education, Experience |
| **🏠 Housing** | 3 | Owns Car, Owns House, Housing Type |
| **👨‍👩‍👧‍👦 Family** | 2 | Family Status, Suite Type |
| **🌍 Regional** | 3 | Population, Region Rating |
| **🏦 Credit Bureau** | 6 | Credit Requests by Time |
| **👥 Social Circle** | 4 | Friends with Problems |
| **⏰ Application Time** | 2 | Day, Hour of Application |
| **📞 Contact Info** | 6 | Phone, Email Availability |

---

## Slide 6: Data Preprocessing

### 🔧 Processing Steps

1. **🔍 Missing Values Analysis**
   - Found columns with missing data
   - Removed columns with >50% missing values

2. **📝 Fill Missing Values**
   - **Numbers** → median value
   - **Categories** → most common value

3. **🔄 Encoding**
   - **Categories** → numbers (LabelEncoder)
   - **Numbers** → scaled (StandardScaler)

### ✅ Result
- **307,507 records** processed
- **40 features** prepared
- **0 missing values** remaining
- **Ready for machine learning**

---

## Slide 7: Target Variable Analysis

### 📊 Default Distribution

```
TARGET Distribution:
├── ✅ No Default (0): 282,686 records (91.9%)
└── ❌ Default (1): 24,821 records (8.1%)

Imbalance Ratio: 11.4:1
```

### 🎯 Key Observations
- **8% default rate** - normal for credit data
- **Unbalanced classes** - need special techniques
- **Most people pay back** their loans

---

## Slide 8: Statistical Analysis

### 📈 Main Statistics

| Feature | Mean | Median | What It Means |
|---------|------|--------|---------------|
| **AMT_INCOME_TOTAL** | 168,797 | 147,000 | Customer income |
| **AMT_CREDIT** | 599,025 | 513,000 | Loan amount |
| **AMT_ANNUITY** | 27,106 | 24,975 | Monthly payment |
| **DAYS_BIRTH** | -15,653 | -15,700 | Customer age |

### 💡 Interpretation
- **Large income variation** - different customer types
- **High loan amounts** - big financial decisions
- **Standardization needed** - different scales

---

## Slide 9: Correlation Analysis

### 🔗 Top 10 Correlations with TARGET

| Feature | Correlation | What It Means |
|---------|-------------|---------------|
| **EXT_SOURCE_3** | -0.178 | External credit score 3 |
| **EXT_SOURCE_2** | -0.160 | External credit score 2 |
| **DAYS_BIRTH** | 0.078 | Customer age |
| **AMT_INCOME_TOTAL** | -0.072 | Total income |
| **AMT_ANNUITY** | -0.065 | Monthly payment |
| **AMT_CREDIT** | -0.060 | Loan amount |
| **REGION_POPULATION_RELATIVE** | -0.055 | Population density |
| **DAYS_EMPLOYED** | -0.052 | Work experience |
| **CNT_FAM_MEMBERS** | 0.048 | Family size |
| **AMT_GOODS_PRICE** | -0.045 | Goods price |

### 🎯 Key Insights
- **External sources** most important (EXT_SOURCE_2, EXT_SOURCE_3)
- **Age** increases default risk
- **Income** decreases default risk
- **Financial factors** matter most

---

## Slide 10: Feature Distribution Analysis

### 📊 Key Feature Distributions

**💰 AMT_INCOME_TOTAL (Income):**
- Most people earn 100,000-200,000
- Some very high earners (outliers)
- Higher income = lower default risk

**👤 DAYS_BIRTH (Age):**
- Peak at age 30-40
- Older people = higher default risk
- Clear relationship with default

**🏦 AMT_CREDIT (Loan Amount):**
- Most loans 300,000-800,000
- Higher amounts = higher risk
- Correlates with income

---

## Slide 11: Important Features Analysis

### 🏆 Top 15 Most Important Features

1. **📊 EXT_SOURCE_3** - External credit score 3
2. **📊 EXT_SOURCE_2** - External credit score 2
3. **👤 DAYS_BIRTH** - Customer age
4. **💰 AMT_INCOME_TOTAL** - Total income
5. **💳 AMT_ANNUITY** - Monthly payment
6. **🏦 AMT_CREDIT** - Loan amount
7. **🌍 REGION_POPULATION_RELATIVE** - Population density
8. **💼 DAYS_EMPLOYED** - Work experience
9. **👨‍👩‍👧‍👦 CNT_FAM_MEMBERS** - Family size
10. **🛒 AMT_GOODS_PRICE** - Goods price
11. **🏠 NAME_HOUSING_TYPE** - Housing type
12. **👤 CODE_GENDER** - Gender
13. **👨‍👩‍👧‍👦 CNT_CHILDREN** - Number of children
14. **💼 NAME_INCOME_TYPE** - Income type
15. **🎓 NAME_EDUCATION_TYPE** - Education level

### 💡 Key Insights
- **External data sources** critically important
- **Demographics** play key role
- **Financial indicators** significant for prediction

---

## Slide 12: Conclusions and Hypotheses

### 🎯 Main Conclusions

1. **⚖️ Unbalanced data** requires special techniques
2. **📊 External sources** most informative
3. **👤 Age and income** key demographic factors
4. **💰 Financial indicators** important for risk assessment
5. **🏠 Housing and family** status matters

### 🔮 Hypotheses for SIS2

1. **⚖️ Balanced models** will show better results
2. **🤝 Ensemble algorithms** will outperform single models
3. **🔧 Feature engineering** will improve prediction quality
4. **📊 External sources** will be key predictors
5. **🎯 Top 20 features** will be enough for good models

---

## Slide 13: Next Steps (SIS2)

### 🚀 Plan for SIS2

1. **🤖 Build Models**
   - Logistic Regression
   - Random Forest
   - XGBoost
   - Neural Networks

2. **📊 Evaluate Quality**
   - Accuracy, Precision, Recall
   - F1-score, ROC-AUC
   - Cross-validation

3. **⚙️ Optimize**
   - Hyperparameter tuning
   - Feature selection
   - Ensemble methods

4. **🔍 Interpret**
   - Feature importance
   - SHAP values
   - Business insights

---

## Slide 14: Technical Details

### 💻 Technologies Used

- **Python 3.11**
- **Pandas, NumPy** - data processing
- **Scikit-learn** - machine learning
- **Matplotlib, Seaborn** - visualization
- **Jupyter Notebooks** - development

### 📁 Project Structure
```
DataMining_SIS1_Project/
├── 📁 data_raw/              # Original data
├── 📁 data_processed/        # Processed data
├── 📁 notebooks/             # Jupyter notebooks
├── 📁 presentation/          # Presentation
├── 📁 reports/               # Reports
├── 📁 scripts/               # Helper scripts
└── 📄 README.md              # Documentation
```

---

## Slide 15: Thank You!

### ✅ SIS1 Key Achievements

✅ **Loaded and processed** real credit company data  
✅ **Selected 40 best features** from 122 original  
✅ **Conducted complete EDA** with key factor identification  
✅ **Prepared quality dataset** for model training  
✅ **Formulated hypotheses** for further research  

### 🚀 Ready for SIS2
- **Processed data** ready for use
- **Important features** identified
- **Understanding** of task and data
- **Clear plan** for next steps

### ❓ Questions?

---

## Appendix: Additional Information

### 📊 Feature Selection Results

**Original Dataset:** 122 features  
**After Selection:** 40 features  
**Reduction:** 67%  
**Quality:** Improved (removed noise)

### 🎯 Why This Approach Works

1. **Faster training** - less data to process
2. **Better accuracy** - focus on important features
3. **Easier interpretation** - fewer features to understand
4. **Less overfitting** - simpler models

### 📈 Expected SIS2 Results

- **Accuracy:** >80%
- **AUC-ROC:** >0.75
- **Key Features:** Top 20 will be sufficient
- **Best Model:** Ensemble of multiple algorithms

---

*Presentation prepared for SIS1 defense in Data Mining course*
*Team: Namazbek, Shyntas, Ibragim*
*Date: 21.10.25*