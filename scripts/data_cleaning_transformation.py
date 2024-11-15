import os
import json
import pandas as pd

os.chdir("../")

# Paths
DATA_DIR = "scraped_data"
CONSOLIDATED_JSON = os.path.join(DATA_DIR, "all_channels_data.json")
CLEANED_CSV = os.path.join(DATA_DIR, "cleaned_data.csv")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Step 1: Convert JSON to CSV
def json_to_csv(json_file, csv_file):
    """Converts a JSON file to CSV format."""
    if not os.path.exists(json_file):
        print(f"Error: JSON file '{json_file}' not found. Please check the scraping script.")
        return
    try:
        with open(json_file, "r") as f:
            data = [json.loads(line) for line in f]
        df = pd.DataFrame(data)
        df.to_csv(csv_file, index=False)
        print(f"Converted JSON to CSV: {csv_file}")
    except Exception as e:
        print(f"Error converting JSON to CSV: {e}")

# Step 2: Enhance Duplicate Detection and Removal
def remove_duplicates(csv_file):
    """Removes duplicate rows from the CSV."""
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found. Run JSON to CSV conversion first.")
        return
    try:
        df = pd.read_csv(csv_file)
        initial_count = len(df)
        df = df.drop_duplicates()
        final_count = len(df)
        print(f"Removed {initial_count - final_count} duplicate rows.")
        df.to_csv(csv_file, index=False)
    except Exception as e:
        print(f"Error removing duplicates: {e}")

# Step 3: Handle Missing Values
def handle_missing_values(csv_file):
    """Handles missing values in the CSV."""
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found. Run JSON to CSV conversion first.")
        return
    try:
        df = pd.read_csv(csv_file)
        # Fill missing values in 'text' with "No text provided"
        df['text'] = df['text'].fillna("No text provided")
        # Fill missing dates with the earliest available date
        earliest_date = pd.to_datetime(df['date'].dropna()).min()
        df['date'] = pd.to_datetime(df['date'], errors='coerce').fillna(earliest_date)
        df.to_csv(csv_file, index=False)
        print("Handled missing values.")
    except Exception as e:
        print(f"Error handling missing values: {e}")

# Step 4: Standardize and Validate Data Formats
def standardize_data_formats(csv_file):
    """Standardizes and validates data formats in the CSV."""
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found. Run JSON to CSV conversion first.")
        return
    try:
        df = pd.read_csv(csv_file)
        # Ensure date is in ISO format
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%dT%H:%M:%S')
        # Validate and clean text field (e.g., remove extra spaces)
        df['text'] = df['text'].str.strip()
        df.to_csv(csv_file, index=False)
        print("Standardized data formats.")
    except Exception as e:
        print(f"Error standardizing data formats: {e}")

# Run the pipeline
if __name__ == "__main__":
    # Ensure the required directory exists
    print(f"Data directory '{DATA_DIR}' checked or created successfully.")
    #  Convert JSON to CSV
    json_to_csv(CONSOLIDATED_JSON, CLEANED_CSV)
    
    # Remove duplicates
    remove_duplicates(CLEANED_CSV)
    
    # Handle missing values
    handle_missing_values(CLEANED_CSV)
    
    #  Standardize and validate data formats
    standardize_data_formats(CLEANED_CSV)
