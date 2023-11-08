<br/>
<p align="center">
  <a href="https://github.com/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset">
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Quarterly Quest: Dive Deep into Data and Discover Trends!</h3>

  <p align="center">
    Analyze. Visualize. Strategize. Elevate Your Quarterlies with Precision and Insight!
    <br/>
    <br/>
    <a href="https://github.com/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset">View Demo</a>
    .
    <a href="https://github.com/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset/issues">Report Bug</a>
    .
    <a href="https://github.com/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset/total) ![Contributors](https://img.shields.io/github/contributors/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset?color=dark-green) ![Stargazers](https://img.shields.io/github/stars/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset?style=social) ![Issues](https://img.shields.io/github/issues/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset) ![License](https://img.shields.io/github/license/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Description

**Title**: Analysis and Visualization of COVID-19 Case Trends

**Background**: The COVID-19 pandemic has led to an unprecedented collection of data as governments, researchers, and healthcare organizations track the spread of the virus. Analyzing this data is critical for understanding the trends of the pandemic and making informed decisions.

**Objective**: The aim is to develop a Python script that can load COVID-19 case data from a CSV file, preprocess the data, inspect it, compute the 75th percentile of new cases, and visualize the trend of new COVID-19 cases over time.

**Data**: The CSV file `covid-data.csv` is expected to contain the following columns:
- `iso_code`: ISO code for the country
- `continent`: The continent where the country is located
- `location`: The name of the country
- `date`: The date of the data entry
- `total_cases`: The cumulative number of COVID-19 cases
- `new_cases`: The number of new COVID-19 cases reported on that date

**Challenges**:
1. Handling various potential issues with file loading such as missing file, empty data, or unexpected errors.
2. Preprocessing the data by selecting relevant columns and converting date strings to datetime objects.
3. Ensuring the data is clean and ready for analysis, which involves handling missing values.
4. Computing statistical measures like the 75th percentile for the new cases to understand the distribution.
5. Visualizing the trend of new COVID-19 cases in a way that is performant and informative.

### Solution Approach

To address the objectives and challenges outlined above, the following Python script has been created. It uses `pandas`, `numpy`, and `matplotlib` to achieve its goals.

```python
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
```

### Solution Explanation

1. **Data Loading**: The `load_data` function is used to read the CSV file. It includes error handling to provide useful feedback in case the file is not found, is empty, or other errors occur.

2. **Preprocessing**: The `preprocess_data` function selects only the relevant columns and converts the date

 column to `datetime` objects, which is essential for chronological analysis and plotting.

3. **Data Inspection**: The `inspect_data` function prints out the first few entries, the data types of each column, and the DataFrame's shape to give a quick overview of the data and its structure.

4. **Quartile Calculation**: The `calculate_quartile` function computes the 75th percentile of new cases, which is a measure of the upper range of daily new cases, indicating a point below which 75% of the data falls.

5. **Visualization**: The `plot_new_cases_trend` function visualizes the trend of new cases. It plots a line chart showing how the number of new cases changes over time.

6. **Performance Check**: The script only plots the data if the DataFrame is smaller than 10,000 rows to avoid performance issues that can arise when plotting large datasets.

7. **Main Script**: The functions are called in a logical sequence after checking that the data is loaded correctly.

By following this approach, the script addresses the challenges posed by the problem and offers a comprehensive solution for the analysis and visualization of COVID-19 case data.

The provided Python script is designed to perform several operations on COVID-19 case data using pandas, numpy, and matplotlib libraries. Here's a breakdown of its logic and functionality:

1. **Importing Required Libraries:**
    - `numpy` as `np`: Used for numerical operations, particularly for calculating the quartile in this script.
    - `pandas` as `pd`: Used for loading and manipulating data in DataFrame format.
    - `matplotlib.pyplot` as `plt`: Used for plotting the trends of new COVID-19 cases.

2. **Defining Functions:**

    - `load_data(file_path)`: This function takes a file path as input and attempts to load the data into a pandas DataFrame using `pd.read_csv`. It handles various exceptions that might occur during file loading, such as `FileNotFoundError` if the file does not exist, `pd.errors.EmptyDataError` if the file is empty, or any other `Exception`. If an exception occurs, it prints an error message and returns `None`.

    - `preprocess_data(df)`: The function takes a DataFrame as input and performs preprocessing tasks. It selects a subset of columns that are relevant to the analysis. It then converts the 'date' column to datetime format, handling any errors by coercing them (i.e., treating errors as `NaT` values). Finally, it makes sure that missing values in 'new_cases' are handled properly, although in the given code, this step doesn't actually change or impute any missing values.

    - `inspect_data(df)`: This function performs a basic inspection of the DataFrame, printing the first five entries with `df.head()`, showing the data types of each column with `df.dtypes`, and printing the shape of the DataFrame with `df.shape`.

    - `calculate_quartile(df, column)`: This function calculates the 75th percentile (also known as the third quartile) of the specified column in the DataFrame. It uses `np.quantile` and excludes any `NaN` values with `dropna()`. If the column doesn't exist, it catches the `KeyError` and returns `None`.

    - `plot_new_cases_trend(df)`: The function is responsible for plotting the trend of new COVID-19 cases over time. It sorts the DataFrame by the 'date' column and plots 'new_cases' against 'date'. It sets up the labels and title of the plot and uses `plt.show()` to display it.

3. **Executing the Analysis:**
    - A file path is specified for the CSV file containing the COVID-19 data.
    - The `load_data` function is called with the file path, and if the data is successfully loaded, the script proceeds.
    - The loaded DataFrame is then passed to the `preprocess_data` function.
    - Next, `inspect_data` is called to display basic information about the DataFrame.
    - The `calculate_quartile` function is called to find the 75th percentile of new cases, and the result is printed.
    - Finally, if the DataFrame has fewer than 10,000 rows, the `plot_new_cases_trend` function is called to visualize the trend of new cases over time. This check is probably in place to avoid performance issues when plotting a large number of data points.

4. **Potential Issues and Considerations:**
    - The `preprocess_data` function seems redundant in its current handling of 'new_cases'; it assigns 'new_cases' to itself when not `NaN`, which is effectively a no-operation.
    - The script assumes that the CSV file contains columns with specific names; if these names are not present, the script may fail.
    - The check `if covid_data is not None` ensures that the following operations are only performed if the data was loaded successfully.
    - The conditional plot based on the size of the DataFrame is a basic form of performance management, as plotting a very large dataset can be resource-intensive.
    - Error handling in the `load_data` function provides robust feedback for common data loading issues, which can be helpful in debugging and operational scenarios.

## Built With

This section of the README file is dedicated to acknowledging the technologies and tools used in the development of the COVID-19 Data Analysis and Visualization project. Understanding the components and libraries involved can help users and contributors set up their environments correctly and appreciate the context in which the project operates.

## Core Language

- **Python** - The entire project is written in Python, a versatile and widely-used programming language known for its readability and broad support of libraries for data analysis and visualization.

## Libraries and Frameworks

The project leverages several powerful Python libraries to handle data manipulation, calculation, and visualization tasks:

- **NumPy** - An essential library for scientific computing in Python. It provides support for arrays (including multi-dimensional arrays), matrices, and a large collection of high-level mathematical functions to operate on these data structures.

  - Website: [numpy.org](https://numpy.org/)
  - Installation command: `pip install numpy`

- **pandas** - An open-source data analysis and manipulation tool, built on top of Python. It offers data structures and operations for manipulating numerical tables and time series, making it a perfect tool for data preprocessing in this project.

  - Website: [pandas.pydata.org](https://pandas.pydata.org/)
  - Installation command: `pip install pandas`

- **Matplotlib** - A plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications.

  - Website: [matplotlib.org](https://matplotlib.org/)
  - Installation command: `pip install matplotlib`

## Development Tools

The following tools are essential in the development, testing, and maintenance of the project:

- **Git** - A distributed version control system used to track changes in the source code during development. It is designed to handle everything from small to very large projects with speed and efficiency.

  - Website: [git-scm.com](https://git-scm.com/)

- **GitHub** - A web-based platform used for version control. It simplifies the use of Git and provides a place to host and collaborate on projects.

  - Website: [github.com](https://github.com/)

## Data

The data used for analysis in this project is from COVID-19 datasets, which usually consist of:

- **CSV Files** - The datasets are typically stored in CSV (Comma-Separated Values) format, which is a simple file format used to store tabular data, such as a spreadsheet or database.

  - Example data source: [Our World in Data](https://ourworldindata.org/coronavirus)

## Additional Tools

These tools are not required but can enhance the experience of using or contributing to the project:

- **Jupyter Notebook** - An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. Useful for data cleaning and transformation, numerical simulation, statistical modeling, data visualization, and much more.

  - Website: [jupyter.org](https://jupyter.org/)
  - Installation command: `pip install notebook`

- **Anaconda** - A distribution of Python and R for scientific computing and data science. It simplifies package management and deployment and comes with a suite of pre-installed libraries for data science.

  - Website: [anaconda.com](https://www.anaconda.com/)

## Contributing Packages

For those looking to contribute to the project, familiarity with the following packages can be beneficial:

- **pytest** - A framework that makes it easy to write simple tests, yet scales to support complex functional testing.

  - Website: [pytest.org](https://pytest.org/)
  - Installation command: `pip install pytest`

- **Black** - The uncompromising Python code formatter that takes total control over the formatting of the code in the project.

  - Website: [black.readthedocs.io](https://black.readthedocs.io/)
  - Installation command: `pip install black`

## Versioning

- **SemVer** - For versioning, the project adheres to Semantic Versioning.

  - Website: [semver.org](https://semver.org/)

This "Built With" section gives a comprehensive overview of the technologies and tools used in the creation of the COVID-19 Data Analysis and Visualization project, ensuring that users and contributors are informed and can set up their development environments accordingly.

## Getting Started

# Getting Started Guide for COVID-19 Data Analysis and Visualization

Welcome to the COVID-19 Data Analysis and Visualization GitHub repository. This guide will walk you through the initial setup and usage of the Python script designed to load, preprocess, inspect, calculate statistics, and visualize COVID-19 case data.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your machine:

- Python (3.6 or higher recommended)
- Pip (Python package installer)

You will also need the following Python libraries:

- NumPy
- pandas
- Matplotlib

If you don't have these libraries installed, you can install them using pip:

```bash
pip install numpy pandas matplotlib
```

## Installation

1. **Clone the Repository**

   To get started, clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. **Data File**

   The script expects a CSV file named `covid-data.csv` containing COVID-19 case data. Ensure that this file is placed in the root of the cloned repository directory.

3. **Running the Script**

   With Python installed and the CSV file in place, you can run the script directly from the command line:

   ```bash
   python covid_analysis.py
   ```

   Replace `covid_analysis.py` with the actual name of the script if it's different.

## Usage

### Loading Data

The script starts by loading the data from the `covid-data.csv` file using the `load_data` function. If the file is not found, is empty, or an error occurs, the function will print a message and return `None`.

### Preprocessing Data

After loading, the `preprocess_data` function is called to select the relevant columns and convert the date column to datetime objects, which allows for time series analysis later on.

### Inspecting Data

Once the data is preprocessed, you can call the `inspect_data` function to print the first five entries of the dataset, the data types of each column, and the shape of the DataFrame.

### Calculating Quartile

The `calculate_quartile` function computes the 75th percentile of the 'new_cases' column to give a sense of the upper range of new daily cases.

### Plotting Data

If the dataset is small enough (fewer than 10,000 rows), the `plot_new_cases_trend` function will plot the trend of new COVID-19 cases over time. This visual representation helps to understand the spread and trends of the virus.

## Contributions

We welcome contributions from the community! If you have suggestions or improvements, please fork the repository, make your changes, and submit a pull request.

For major changes, please open an issue first to discuss what you would like to change. Ensure to update tests as appropriate.

## Support

If you encounter any problems or have any inquiries, please open an issue in the repository with a description of the issue or question you have.

Thank you for using or contributing to this COVID-19 data analysis project!

---

Please note that this guide assumes a certain level of familiarity with command-line operations, Python programming, and version control with Git. If you need assistance with any of these topics, we recommend searching for an online tutorial or guide that fits your learning style and experience level.

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/ TribeOfJudahLion/Analyzing-The-Quartiles-Of-A-Dataset/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
