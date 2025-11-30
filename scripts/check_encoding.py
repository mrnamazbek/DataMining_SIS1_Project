#!/usr/bin/env python3
"""
Script to check file encoding and fix encoding issues
"""

import pandas as pd
import chardet

def detect_encoding(file_path):
    """Detect file encoding"""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def load_csv_with_encoding(file_path):
    """Load CSV with automatic encoding detection"""
    try:
        # Try UTF-8 first
        df = pd.read_csv(file_path, encoding='utf-8')
        print(f"Successfully loaded with UTF-8 encoding")
        return df
    except UnicodeDecodeError:
        try:
            # Try Latin-1
            df = pd.read_csv(file_path, encoding='latin-1')
            print(f"Successfully loaded with Latin-1 encoding")
            return df
        except UnicodeDecodeError:
            try:
                # Try CP1252
                df = pd.read_csv(file_path, encoding='cp1252')
                print(f"Successfully loaded with CP1252 encoding")
                return df
            except UnicodeDecodeError:
                # Detect encoding automatically
                encoding = detect_encoding(file_path)
                print(f"Detected encoding: {encoding}")
                df = pd.read_csv(file_path, encoding=encoding)
                print(f"Successfully loaded with detected encoding: {encoding}")
                return df

if __name__ == "__main__":
    file_path = '../data_raw/HomeCredit_columns_description.csv'
    
    print(f"Checking file: {file_path}")
    print(f"Detected encoding: {detect_encoding(file_path)}")
    
    # Load the file
    df = load_csv_with_encoding(file_path)
    print(f"File loaded successfully: {df.shape}")
    print(f"First few rows:")
    print(df.head())
