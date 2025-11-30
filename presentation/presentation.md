# Home Credit Default Risk Prediction
## SIS 2: Data Mining Techniques & Evaluation

---

## 1. Introduction & Background
- **Goal**: Predict loan default risk (`TARGET` variable).
- **Problem**: Binary Classification (0 = Repaid, 1 = Default).
- **Context**: Helping Home Credit Group predict clients' repayment abilities to broaden financial inclusion.

---

## 2. Dataset & Preprocessing (Recap)
*(From SIS 1)*
- **Dataset Size**: 307,511 rows, 42 selected features.
- **Key Features**: `EXT_SOURCE`, `DAYS_BIRTH`, `AMT_CREDIT`, `DAYS_EMPLOYED`.
- **Preprocessing Steps**:
    - **Cleaning**: Imputed missing values.
    - **Encoding**: Label Encoding (binary), One-Hot Encoding (categorical).
    - **Scaling**: Standardized numerical features.
    - **Selection**: Filtered top 42 features based on correlation/importance.
- **Challenge**: Class Imbalance (8.07% positive class).

---

## 3. Methodology (Algorithms Used)
We applied 5 classification algorithms:

1.  **Logistic Regression**: Baseline linear model.
2.  **Decision Tree**: Simple non-linear model.
3.  **Random Forest**: Bagging ensemble (reduces variance).
4.  **Gradient Boosting**: Boosting ensemble (reduces bias).
5.  **Gaussian Naive Bayes**: Fast probabilistic baseline.

**Metrics**: ROC-AUC (primary), Precision, Recall, F1-Score.

---

## 4. Hyperparameter Tuning
We optimized the **Random Forest** model using `RandomizedSearchCV`.

**Hyperparameters Changed**:
- `n_estimators` (100 -> 300): More trees for stability.
- `max_depth` (10 -> 30): Controls model complexity.
- `min_samples_split` (2 -> 10): Prevents overfitting.

**Impact**:
- Increasing `max_depth` improved training AUC but plateaued on test AUC around depth=15.
- Tuning improved ROC-AUC by ~0.02 over the baseline.

---

## 5. Model Comparison
| Model | Accuracy | ROC AUC | F1 Score |
|-------|----------|---------|----------|
| **Gradient Boosting** | 0.92 | **0.75** | 0.28 |
| **Random Forest (Tuned)** | 0.91 | **0.74** | 0.26 |
| Logistic Regression | 0.68 | 0.72 | 0.23 |
| Naive Bayes | 0.35 | 0.65 | 0.18 |
| Decision Tree | 0.85 | 0.54 | 0.14 |

*Note: Gradient Boosting and Tuned Random Forest performed best.*

---

## 6. Results & Interpretation
- **Confusion Matrix**: Shows we can detect ~65% of defaulters (Recall) but with some false alarms.
- **Key Features**:
    - `EXT_SOURCE_2` & `EXT_SOURCE_3` are the strongest predictors.
    - `DAYS_BIRTH`: Younger people are higher risk.
- **Business Impact**:
    - Using the **Gradient Boosting** model allows the bank to reject high-risk applications more accurately, reducing financial loss while maintaining approval rates for creditworthy clients.
