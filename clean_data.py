import os
import pandas as pd
from datetime import datetime

# Define input and output folders
input_folder = 'input/'
output_folder = 'output/'

# Function to clean data
def clean_data(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Automatically handle missing values and duplicates
    df_cleaned = df.dropna()  # Drop rows with missing values
    df_cleaned = df_cleaned.drop_duplicates()  # Remove duplicate rows
    
    # Generate a new filename for the cleaned data
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(file_path)
    output_file = os.path.join(output_folder, f'cleaned_{timestamp}_{filename}')
    
    # Save the cleaned data to a new CSV file
    df_cleaned.to_csv(output_file, index=False)
    print(f"Data cleaning completed. Cleaned data saved to {output_file}.")
    
# Function to process all files in the input folder
def process_input_files():
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        if file.endswith(".csv"):
            print(f"Processing file: {file}")
            clean_data(file_path)

if __name__ == "__main__":
    process_input_files()
