import os
import re
import pandas as pd

# ============================
# Configuration
# ============================

# Enter the CSV export URL
csv_url = "Enter your CSV URL here"

# Replace with your spreadsheet column names
FOLDER_COLUMN = "Folder Column"
CONTENT_COLUMN = "Content Column"

# Output configuration
OUTPUT_DIR = "Output"
FILE_NAME = "file.txt"

# ============================
# Read CSV
# ============================

df = pd.read_csv(csv_url)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================
# Helper Function
# ============================

def clean_filename(name):
    return re.sub(r'[<>:"/\\|?*]', "_", str(name))

# ============================
# Generate Folders & Files
# ============================

for _, row in df.iterrows():

    folder_name = str(row[FOLDER_COLUMN]).strip()
    file_content = str(row[CONTENT_COLUMN]).strip()

    if not folder_name:
        continue

    folder_path = os.path.join(OUTPUT_DIR, clean_filename(folder_name))
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, FILE_NAME)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(file_content)

    print(f"Created: {file_path}")

print("Done!")
