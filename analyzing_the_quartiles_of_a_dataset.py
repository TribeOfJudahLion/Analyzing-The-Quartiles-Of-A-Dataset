# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function Definitions

# Function to load data from a CSV file
def load_data(file_path):
    """
    Load the data from a CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return df

# Function to preprocess data
def preprocess_data(df):
    """
    Preprocess the data, selecting relevant columns and handling missing values.
    """
    columns = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases']
    df = df.loc[:, columns].copy()
    df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)
    return df

# Function to inspect data
def inspect_data(df):
    """
    Perform a basic inspection of the dataframe.
    """
    print("First 5 entries in the dataset:")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)
    print("\nDataframe Shape:")
    print(df.shape)

# Function to calculate the 75th percentile
def calculate_quartile(df, column):
    """
    Calculate the 75th percentile of a given column in the dataframe.
    """
    try:
        quartile = np.quantile(df[column].dropna(), 0.75)
        return quartile
    except KeyError:
        print(f"Column {column} does not exist in the dataframe.")
        return None

# Function to plot the trend of new cases
def plot_new_cases_trend(df):
    """
    Plot the trend of new COVID-19 cases over time.
    """
    df.sort_values('date', inplace=True)
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['new_cases'], label='New Cases')
    plt.xlabel('Date')
    plt.ylabel('Number of New Cases')
    plt.title('Trend of New COVID-19 Cases')
    plt.legend()
    plt.show()

# Main Execution

file_path = "covid-data.csv"
covid_data = load_data(file_path)

if covid_data is not None:
    covid_data = preprocess_data(covid_data)
    inspect_data(covid_data)
    quartile = calculate_quartile(covid_data, "new_cases")
    print(f"\n75th percentile of new cases: {quartile}")

    if covid_data.shape[0] < 10000:
        plot_new_cases_trend(covid_data)
