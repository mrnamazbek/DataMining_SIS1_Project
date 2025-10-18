# 🏦 Data Mining Project — Home Credit Default Risk Prediction

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=36BCF7&lines=Credit+Risk+Prediction;Machine+Learning;Data+Mining;Financial+Analytics)](https://git.io/typing-svg)

---

## 📌 Project Overview  
Этот проект является частью курса **Data Mining @ KBTU (MSc Program)**.  
Мы анализируем датасет **Home Credit Default Risk** с Kaggle и строим модели для предсказания способности клиентов возвращать кредиты.  

**Датасет:** [Home Credit Default Risk](https://www.kaggle.com/competitions/home-credit-default-risk)  

### ✅ Почему этот датасет?  
- **Открытый и надежный** → Официальный датасет соревнования Kaggle  
- **Размер** → Более **300,000+ записей**  
- **Богатство данных** → Более **120 признаков** включая демографические, кредитные и поведенческие данные  
- **Реальная значимость** → Предсказание кредитного риска - одна из важнейших задач в банковской сфере и финтехе  

---

## 🎯 Требования проекта  

- Более **14 признаков** ✅  
- Более **40,000 записей** ✅  
- Открытый датасет ✅  
- Групповой проект (макс. 3 студента) ✅  

---

## 📑 Результаты проекта  

### Часть 1 – SIS 1 ✅ ЗАВЕРШЕНО

1. **Project Proposal** ✅  
   - Описание проблемы и целей  
   - Исследовательские вопросы и гипотезы  
   - Обоснование выбора датасета  

2. **Работа с данными** ✅  
   - Загрузка данных (с Kaggle)  
   - Описание датасета (размер, признаки, тип, источник)  
   - Очистка данных (пропущенные значения, выбросы, несоответствия)  
   - Преобразование данных (масштабирование, кодирование, отбор признаков)  

3. **Exploratory Data Analysis (EDA)** ✅  
   - Описательная статистика (среднее, дисперсия, распределение)  
   - Корреляции между переменными  
   - Визуализации (гистограммы, scatter plots, тепловые карты)  
   - Первичные инсайты  

4. **Презентация** ✅  
   - Описание проблемы  
   - Датасет  
   - Этапы предобработки  
   - Результаты EDA  

---

### Часть 2 – SIS 2 🔄 В ПЛАНАХ

1. **Техники Data Mining**  
   - Применение **4–5 алгоритмов** (классификация/регрессия)  
   - Обоснование выбора алгоритмов  

2. **Оценка и сравнение моделей**  
   - Метрики: Accuracy, Precision/Recall, RMSE, AUC  
   - Cross-validation или train-test split  
   - Сравнение производительности  

3. **Результаты и интерпретация**  
   - Матрица ошибок, ROC кривая, важность признаков  
   - Выделение ключевых инсайтов  
   - Обсуждение реального значения результатов  

4. **Презентация**  
   - Введение и предыстория  
   - Датасет и предобработка (повтор)  
   - Методология (алгоритмы)  
   - Результаты и оценка  

---

## 🛠️ Tech Stack  

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

## 📁 Структура проекта  

```
DataMining_SIS1_Project/
├── data_raw/                    # Исходные данные (CSV файлы)
│   ├── application_train.csv    # Основные данные для обучения
│   ├── application_test.csv     # Тестовые данные
│   ├── bureau.csv              # Кредитная история
│   └── ...
├── data_processed/              # Обработанные данные
│   ├── train_processed.csv      # Обработанные данные для обучения
│   ├── test_processed.csv       # Обработанные тестовые данные
│   └── feature_info.json       # Информация о признаках
├── notebooks/                    # Jupyter ноутбуки
│   ├── 01_data_preprocessing.ipynb  # Предобработка данных
│   └── 02_eda.ipynb            # Exploratory Data Analysis
├── presentation/                 # Презентация для защиты
│   └── sis1_presentation.md     # Слайды презентации
├── reports/                      # Отчеты и документация
│   └── project_proposal.md      # Project Proposal
├── scripts/                      # Вспомогательные Python скрипты
├── models/                       # Сохраненные модели (SIS2)
├── requirements.txt              # Зависимости Python
└── README.md                     # Документация проекта
```

---

## 🚀 Дорожная карта проекта  

### ✅ SIS 1 - ЗАВЕРШЕНО
1. **Загрузка и настройка датасета** ✅  
2. **Очистка данных** (пропущенные значения, выбросы) ✅  
3. **Feature engineering** (масштабирование, кодирование, преобразования) ✅  
4. **Exploratory Data Analysis (EDA)** с визуализациями ✅  
5. **Подготовка презентации** ✅  

### 🔄 SIS 2 - В ПЛАНАХ
6. **Моделирование** с несколькими алгоритмами  
7. **Оценка** (метрики, сравнение)  
8. **Интерпретация и презентация**  

---

## 📊 Ключевые результаты SIS1  

### 📈 **Статистика датасета**
- **307,507 записей** клиентов
- **122 признака** (демографические, финансовые, кредитные)
- **8.1% дефолтов** (несбалансированные данные)
- **0 пропущенных значений** после обработки

### 🔍 **Ключевые инсайты**
- **Внешние источники данных** (EXT_SOURCE_1,2,3) наиболее информативны
- **Возраст клиента** положительно коррелирует с дефолтом
- **Доход** отрицательно коррелирует с риском
- **Финансовые показатели** критически важны для прогноза

### 🛠️ **Технические достижения**
- Полная автоматизация предобработки данных
- Комплексный EDA с визуализациями
- Готовый pipeline для обучения моделей
- Качественная документация и презентация

---

## 📫 Команда и контакты  

👨‍💻 **Namazbek Bekzhanov** — MSc @ KBTU  
📧 [namazbekzhan@gmail.com](mailto:namazbekzhan@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/namazbek-bekzhanov/)  

---

⚙️ *Превращаем сырые данные в реальные инсайты — суть Data Mining.*  
