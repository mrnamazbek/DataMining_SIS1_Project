# Project Explanation - SIS 2: Data Mining Techniques & Evaluation

## 1. Problem Statement & Objectives
The goal of this project is to predict **Home Credit Default Risk**—whether a client will have difficulty repaying a loan. This is a binary classification problem where the target variable is `TARGET` (0: Repaid, 1: Default).

## 2. Dataset & Preprocessing (Recap)
- **Source**: Home Credit Group (Kaggle).
- **Size**: ~307,000 instances.
- **Features**: 42 selected features (after feature selection in SIS 1).
- **Preprocessing**:
    - Handling missing values (imputation).
    - Encoding categorical variables (One-Hot/Label Encoding).
    - Scaling numerical features (StandardScaler).
    - Feature selection (Mutual Information/Correlation).
    - **Class Imbalance**: The dataset is highly imbalanced (only ~8% defaults). We used stratified splitting and class weights in models to handle this.

## 3. Data Mining Techniques (Methodology)
We applied 5 different classification algorithms to solve this problem. Here is the justification for each:

1.  **Logistic Regression**:
    - *Justification*: Serves as a robust **baseline**. It provides interpretability (coefficients) and is computationally efficient. Good for understanding linear relationships.
2.  **Decision Tree**:
    - *Justification*: Captures **non-linear relationships** and interactions between features. Easy to visualize and interpret, though prone to overfitting.
3.  **Random Forest**:
    - *Justification*: An **ensemble method** (Bagging) that reduces the variance of Decision Trees. It is robust to overfitting and generally provides high accuracy.
4.  **Gradient Boosting (GBM)**:
    - *Justification*: An ensemble method (Boosting) that builds models sequentially to correct errors of previous models. Often achieves state-of-the-art performance on tabular data.
5.  **Gaussian Naive Bayes**:
    - *Justification*: A probabilistic classifier based on Bayes' theorem. It assumes feature independence. Used as a fast, simple baseline to compare against more complex models.

## 4. Model Evaluation & Comparison
We evaluated models using a 80-20 Train-Test split with Stratified Sampling.

### Metrics Used:
- **ROC-AUC (Area Under the Receiver Operating Characteristic Curve)**: The primary metric because the dataset is imbalanced. It measures the model's ability to distinguish between classes across all thresholds.
- **Accuracy**: Overall correctness (less reliable for imbalanced data).
- **Precision & Recall**: Important for understanding the trade-off between catching defaults (Recall) and false alarms (Precision).
- **F1-Score**: Harmonic mean of Precision and Recall.

### Hyperparameter Tuning
We performed **RandomizedSearchCV** on the **Random Forest** model to optimize:
- `n_estimators`: Number of trees.
- `max_depth`: Maximum depth of trees (to control overfitting).
- `min_samples_split` & `min_samples_leaf`: Constraints on leaf creation.
- `max_features`: Number of features to consider at each split.

**Impact**: Tuning `max_depth` showed that increasing depth improves training performance but can lead to overfitting on the test set. We found an optimal depth that balances bias and variance.

## 5. Results & Interpretation
### Key Findings:
- **Best Model**: **Gradient Boosting** and **Random Forest** generally outperformed Logistic Regression and Naive Bayes.
- **Key Features**: The most important predictors of default risk were:
    1.  `EXT_SOURCE_2` & `EXT_SOURCE_3`: Normalized scores from external data sources.
    2.  `DAYS_BIRTH`: Age of the client (younger clients tend to be riskier).
    3.  `DAYS_EMPLOYED`: Duration of employment.
    4.  `AMT_GOODS_PRICE` & `AMT_CREDIT`: Loan amount relative to goods price.

### Real-World Meaning:
- The model can help Home Credit identify high-risk applicants *before* granting a loan.
- By focusing on key features like external scores and age, the bank can refine its credit scoring policy.
- The confusion matrix reveals the trade-off: detecting more defaulters (True Positives) comes at the cost of rejecting some good customers (False Positives). The threshold can be adjusted based on the bank's risk appetite.
