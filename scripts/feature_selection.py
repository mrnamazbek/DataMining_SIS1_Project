#!/usr/bin/env python3
"""
Feature Selection Script - Select top 25-30 most important features
"""

import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_classif
import json

def select_important_features():
    """
    Select the most important features for credit risk prediction
    Based on domain knowledge and correlation analysis
    """
    
    # Load processed data
    print("Loading processed data...")
    df = pd.read_csv('data_processed/train_processed.csv')
    
    # Define important feature categories
    important_features = {
        # Basic customer info
        'demographics': [
            'CODE_GENDER',           # Gender
            'DAYS_BIRTH',           # Age (negative days from birth)
            'CNT_CHILDREN',         # Number of children
            'CNT_FAM_MEMBERS',      # Family size
        ],
        
        # Financial information
        'financial': [
            'AMT_INCOME_TOTAL',     # Total income
            'AMT_CREDIT',           # Credit amount
            'AMT_ANNUITY',          # Monthly payment
            'AMT_GOODS_PRICE',      # Goods price
        ],
        
        # External data sources (most important!)
        'external_sources': [
            'EXT_SOURCE_2',         # External source 2 (credit bureau score)
            'EXT_SOURCE_3',         # External source 3 (credit bureau score)
        ],
        
        # Employment and education
        'employment': [
            'DAYS_EMPLOYED',        # Days employed
            'NAME_INCOME_TYPE',     # Income type
            'NAME_EDUCATION_TYPE',  # Education level
            'OCCUPATION_TYPE',      # Occupation
        ],
        
        # Housing and property
        'housing': [
            'NAME_HOUSING_TYPE',    # Housing type
            'FLAG_OWN_CAR',         # Owns car
            'FLAG_OWN_REALTY',      # Owns real estate
        ],
        
        # Family status
        'family': [
            'NAME_FAMILY_STATUS',   # Family status
            'NAME_TYPE_SUITE',      # Type of suite
        ],
        
        # Regional information
        'regional': [
            'REGION_POPULATION_RELATIVE',  # Population relative to region
            'REGION_RATING_CLIENT',        # Region rating
            'REGION_RATING_CLIENT_W_CITY', # Region rating with city
        ],
        
        # Credit bureau information
        'credit_bureau': [
            'AMT_REQ_CREDIT_BUREAU_HOUR',  # Credit bureau requests per hour
            'AMT_REQ_CREDIT_BUREAU_DAY',   # Credit bureau requests per day
            'AMT_REQ_CREDIT_BUREAU_WEEK',  # Credit bureau requests per week
            'AMT_REQ_CREDIT_BUREAU_MON',   # Credit bureau requests per month
            'AMT_REQ_CREDIT_BUREAU_QRT',   # Credit bureau requests per quarter
            'AMT_REQ_CREDIT_BUREAU_YEAR',  # Credit bureau requests per year
        ],
        
        # Social circle (important for risk assessment)
        'social': [
            'OBS_30_CNT_SOCIAL_CIRCLE',    # Observed 30 days social circle
            'DEF_30_CNT_SOCIAL_CIRCLE',    # Defaulted 30 days social circle
            'OBS_60_CNT_SOCIAL_CIRCLE',    # Observed 60 days social circle
            'DEF_60_CNT_SOCIAL_CIRCLE',    # Defaulted 60 days social circle
        ],
        
        # Application timing
        'application_timing': [
            'WEEKDAY_APPR_PROCESS_START',  # Weekday of application
            'HOUR_APPR_PROCESS_START',     # Hour of application
        ],
        
        # Contact information
        'contact': [
            'FLAG_MOBIL',           # Has mobile phone
            'FLAG_EMP_PHONE',      # Has work phone
            'FLAG_WORK_PHONE',     # Has work phone
            'FLAG_CONT_MOBILE',    # Has contact mobile
            'FLAG_PHONE',          # Has phone
            'FLAG_EMAIL',         # Has email
        ]
    }
    
    # Flatten the important features
    selected_features = []
    for category, features in important_features.items():
        selected_features.extend(features)
    
    # Add ID and target
    selected_features = ['SK_ID_CURR', 'TARGET'] + selected_features
    
    # Check which features exist in the dataset
    available_features = [f for f in selected_features if f in df.columns]
    missing_features = [f for f in selected_features if f not in df.columns]
    
    print(f"Selected features: {len(available_features)}")
    print(f"Missing features: {len(missing_features)}")
    if missing_features:
        print(f"Missing: {missing_features}")
    
    # Create feature selection info
    feature_selection_info = {
        'total_original_features': len(df.columns),
        'selected_features_count': len(available_features) - 2,  # Exclude ID and target
        'selected_features': available_features[2:],  # Exclude ID and target
        'feature_categories': important_features,
        'missing_features': missing_features
    }
    
    # Save feature selection info
    with open('data_processed/feature_selection_info.json', 'w') as f:
        json.dump(feature_selection_info, f, indent=2)
    
    print(f"\nFeature selection completed!")
    print(f"Original features: {len(df.columns)}")
    print(f"Selected features: {len(available_features) - 2}")
    print(f"Reduction: {((len(df.columns) - len(available_features) + 2) / len(df.columns) * 100):.1f}%")
    
    return available_features, feature_selection_info

if __name__ == "__main__":
    selected_features, info = select_important_features()
    
    print(f"\nSelected features by category:")
    for category, features in info['feature_categories'].items():
        available_in_category = [f for f in features if f in info['selected_features']]
        print(f"  {category}: {len(available_in_category)} features")
        for feature in available_in_category:
            print(f"    - {feature}")
