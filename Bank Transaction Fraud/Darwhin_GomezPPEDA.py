# Data manipulation and analysis
import pandas as pd  # For data manipulation and cleaning (loading data, filtering, etc.)
import numpy as np   # For numerical operations (e.g., mathematical calculations, arrays)

# Data visualization
import matplotlib.pyplot as plt  # For basic plotting (e.g., histograms, scatter plots)
import seaborn as sns          # For advanced statistical plots and better aesthetics

# Machine learning models
from sklearn.ensemble import IsolationForest  # For anomaly detection (Isolation Forest)
from sklearn.cluster import DBSCAN           # For density-based clustering (DBSCAN)
from sklearn.cluster import KMeans           # For KMeans clustering
from sklearn.preprocessing import StandardScaler  # For standardizing features (important for clustering and anomaly detection)

# For working with dates and times
import datetime  # For handling and manipulating datetime objects (e.g., converting transaction date columns)

# For handling warnings (optional)
import warnings
warnings.filterwarnings('ignore')  # To ignore warnings during model training (can be helpful for large datasets)

# Load the dataset with a meaningful variable name
bank_trans_data = pd.read_csv("bank_transactions_data_2.csv")

# Display the first few rows of the dataset to understand its structure
print("Dataset Preview:")
print(bank_trans_data.head())


# Check the basic info to understand data types and identify any missing values
print("\nDataset Information:")
print(bank_trans_data.info())


# Display summary statistics to get an overview of the data distributions
print("\nSummary Statistics:")
print(bank_trans_data.describe())



# Check for any missing values in the dataset
missing_values = bank_trans_data.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values[missing_values > 0])


unique_counts = bank_trans_data.nunique()
print("Unique Counts for Each Column:")
print(unique_counts)
# Check the data types of all columns
print(bank_trans_data.dtypes)

# Define columns to exclude from categorical analysis
excluded_cols = ['IP Address','TransactionID', 'AccountID', 'MerchantID', 'TransactionDate', 'DeviceID', 'PreviousTransactionDate']

# Select categorical columns, excluding the identifier-like columns
categorical_cols = bank_trans_data.select_dtypes(include=['object']).columns.difference(excluded_cols)

# Display value counts for each remaining categorical column
for col in categorical_cols:
    print(f"\nValue Counts for {col}:")
    print(bank_trans_data[col].value_counts())



# Initial Visualization of Transaction Amount Distribution
sns.histplot(bank_trans_data['TransactionAmount'], kde=True)
plt.title('Transaction Amount Distribution')
plt.show()


# Boxplot to detect outliers in Transaction Amount
plt.figure(figsize=(10, 6))
sns.boxplot(x=bank_trans_data['TransactionAmount'], color='orange')
plt.title('Boxplot of Transaction Amount')
plt.xlabel('Transaction Amount')
plt.show()
#  **Account Balance**
plt.figure(figsize=(10, 6))
sns.histplot(bank_trans_data['AccountBalance'], kde=True, color='red', bins=50)
plt.title('Account Balance Distribution')
plt.xlabel('Account Balance')
plt.ylabel('Frequency')
plt.show()


# Boxplot for Account Balance
plt.figure(figsize=(10, 6))
sns.boxplot(x=bank_trans_data['AccountBalance'], color='cyan')
plt.title('Boxplot of Account Balance')
plt.xlabel('Account Balance')
plt.show()


# 5. **Login Attempts**
plt.figure(figsize=(10, 6))
sns.histplot(bank_trans_data['LoginAttempts'], kde=True, color='brown', bins=30)
plt.title('Login Attempts Distribution')
plt.xlabel('Login Attempts')
plt.ylabel('Frequency')
plt.show()

# Boxplot for Login Attempts
plt.figure(figsize=(10, 6))
sns.boxplot(x=bank_trans_data['LoginAttempts'], color='pink')
plt.title('Boxplot of Login Attempts')
plt.xlabel('Login Attempts')
plt.show()


# 6. **Transaction Duration**
plt.figure(figsize=(10, 6))
sns.histplot(bank_trans_data['TransactionDuration'], kde=True, color='teal', bins=30)
plt.title('Transaction Duration Distribution')
plt.xlabel('Transaction Duration (seconds)')
plt.ylabel('Frequency')
plt.show()


# Boxplot for Transaction Duration
plt.figure(figsize=(10, 6))
sns.boxplot(x=bank_trans_data['TransactionDuration'], color='grey')
plt.title('Boxplot of Transaction Duration')
plt.xlabel('Transaction Duration (seconds)')
plt.show()
# 3. **Customer Age**
plt.figure(figsize=(10, 6))
sns.histplot(bank_trans_data['CustomerAge'], kde=True, color='green', bins=30)
plt.title('Customer Age Distribution')
plt.xlabel('Customer Age')
plt.ylabel('Frequency')
plt.show()


# Boxplot for Customer Age
plt.figure(figsize=(10, 6))
sns.boxplot(x=bank_trans_data['CustomerAge'], color='purple')
plt.title('Boxplot of Customer Age')
plt.xlabel('Customer Age')
plt.show()