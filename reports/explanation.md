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

## 3. Data Mining Techniques (Algorithms) / Алгоритмы

We applied 5 different classification algorithms. Here is why we used them and what they do:

### 1. Logistic Regression (Логистическая регрессия)
*   **English**: This is a simple algorithm used for classification problems. It predicts the probability that an observation belongs to a certain class (e.g., Default or No Default).
    *   *Purpose*: Used as a **baseline** model to compare others against. It's fast and easy to interpret.
*   **Russian**: Это простой алгоритм для задач классификации. Он предсказывает вероятность того, что клиент не вернет кредит.
    *   *Цель*: Используется как **базовая модель** для сравнения. Он быстрый и понятный.

### 2. Decision Tree (Дерево решений)
*   **English**: This algorithm splits the data into branches like a tree to make decisions. It asks a series of "Yes/No" questions to classify data.
    *   *Purpose*: Good for capturing non-linear relationships and is very easy to visualize.
*   **Russian**: Алгоритм делит данные на ветви, как дерево, чтобы принять решение. Он задает серию вопросов "Да/Нет", чтобы классифицировать клиента.
    *   *Цель*: Хорошо находит сложные связи в данных и его легко визуализировать (нарисовать).

### 3. Random Forest (Случайный лес)
*   **English**: This is a collection of many Decision Trees. Each tree gives a vote, and the most popular class is chosen.
    *   *Purpose*: It is much more accurate than a single Decision Tree and prevents overfitting (memorizing the data).
*   **Russian**: Это коллекция из множества Деревьев решений. Каждое дерево "голосует", и выбирается самый популярный вариант.
    *   *Цель*: Он намного точнее, чем одно дерево, и лучше работает на новых данных (не "заучивает" старые).

### 4. Gradient Boosting (Градиентный бустинг)
*   **English**: This algorithm builds models sequentially. Each new model tries to correct the errors made by the previous ones.
    *   *Purpose*: Often provides the **best accuracy** for table data like ours. It learns from mistakes.
*   **Russian**: Алгоритм строит модели по очереди. Каждая новая модель пытается исправить ошибки, сделанные предыдущими.
    *   *Цель*: Часто дает **лучшую точность** для табличных данных. Он "учится на ошибках".

### 5. Naive Bayes (Наивный Байес)
*   **English**: A probabilistic classifier based on Bayes' theorem. It assumes all features are independent (unrelated) to each other.
    *   *Purpose*: Very fast and simple. Used as another baseline.
*   **Russian**: Вероятностный классификатор, основанный на теореме Байеса. Он предполагает, что все признаки не зависят друг от друга.
    *   *Цель*: Очень быстрый и простой. Используется для сравнения.

---

## 4. Results & Comparison / Результаты

We evaluated the models based on several metrics. The most important one for us is **ROC AUC** (because our data is imbalanced).

| ID | Model | Accuracy | Precision | Recall | F1 Score | ROC AUC | Time (s) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 3 | **Gradient Boosting** | 0.919337 | 0.520408 | 0.010272 | 0.020146 | **0.747247** | 43.36 |
| 0 | Logistic Regression | 0.684715 | 0.157632 | 0.668882 | 0.255138 | 0.739590 | 1.60 |
| 2 | **Random Forest** | 0.919191 | 0.419355 | 0.002618 | 0.005204 | 0.721116 | 8.18 |
| 4 | Naive Bayes | 0.121441 | 0.082796 | 0.980665 | 0.152700 | 0.669928 | 0.12 |
| 1 | Decision Tree | 0.860251 | 0.143838 | 0.147633 | 0.145711 | 0.535232 | 3.17 |

### Interpretation / Интерпретация:
*   **Gradient Boosting** is the winner with the highest ROC AUC score (**0.75**). This means it is the best at distinguishing between good and bad clients.
*   **Logistic Regression** has a high Recall (0.67) but low Precision, meaning it catches many defaulters but also falsely accuses many good clients.
*   **Random Forest** is also strong (0.72 AUC) but slightly worse than Gradient Boosting.

## 5. Hyperparameter Tuning
We tuned the **Random Forest** model to improve it further.
*   **Impact**: Tuning `max_depth` showed that increasing depth improves training performance but can lead to overfitting on the test set. We found an optimal depth that balances bias and variance.

## 6. Real-World Meaning
*   The model can help Home Credit identify high-risk applicants *before* granting a loan.
*   By focusing on key features like external scores and age, the bank can refine its credit scoring policy.
