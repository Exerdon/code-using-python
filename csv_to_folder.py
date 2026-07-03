import os
import re
import pandas as pd

# CSV export URL
csv_url = f"Enter your URL here" #Enter your URL here

# Read the sheet
df = pd.read_csv(csv_url)

# Output folder
OUTPUT_DIR = "Tasks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Remove invalid filename characters
def clean_filename(name):
    return re.sub(r'[<>:"/\\\\|?*]', "_", str(name))

for _, row in df.iterrows():
    hero_task = str(row["hero_task"]).strip()
    instructions = str(row["must_follow_instructions"]).strip()

    if not hero_task:
        continue

    folder = os.path.join(OUTPUT_DIR, clean_filename(hero_task))
    os.makedirs(folder, exist_ok=True)

    txt_path = os.path.join(folder, "must_follow_instructions.txt")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(instructions)

    print(f"Created: {txt_path}")

print("Done!")
