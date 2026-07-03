# code-using-python
# Google Sheets Folder Generator

A Python utility that reads data from a public Google Spreadsheet and automatically generates folders and text files based on the values in specified columns.

This project can be adapted to any spreadsheet by changing the column names in the script.

---

## Features

- Read data directly from a public Google Sheet
- Automatically create folders from a spreadsheet column
- Generate text files inside each folder
- Support any spreadsheet structure by changing column names
- Sanitize folder names by replacing invalid filename characters
- No Google API credentials required

---

## Requirements

- Python 3.8+
- pandas

Install the required dependency:

```bash
pip install pandas
```

---

## Project Structure

```
Project/
│
├── main.py
├── README.md
└── Output/
    ├── Folder 1/
    │   └── file.txt
    ├── Folder 2/
    │   └── file.txt
    └── ...
```

---

## How It Works

1. Downloads a Google Spreadsheet as a CSV file.
2. Reads all rows using Pandas.
3. Creates a folder using the value from a chosen column.
4. Creates a text file inside each folder.
5. Writes data from another chosen column into the text file.

---

## Configuration

Update the spreadsheet information:

```python
SPREADSHEET_ID = "YOUR_SPREADSHEET_ID"
GID = "YOUR_SHEET_GID"
```

Then modify the column names to match your spreadsheet:

```python
folder_name = row["Folder Column"]
file_content = row["Content Column"]
```

You can also change:

- Output directory name
- Output file name
- File extension (`.txt`, `.md`, `.json`, etc.)

---

## Running

```bash
python main.py
```

---

## Example

Suppose your spreadsheet contains:

| Folder Name | Description |
|-------------|-------------|
| Project A | Information about Project A |
| Project B | Information about Project B |

The script generates:

```
Output/
│
├── Project A/
│   └── file.txt
│
└── Project B/
    └── file.txt
```

where each `file.txt` contains the corresponding description from the spreadsheet.

---

## Customization Ideas

This project can easily be extended to:

- Create multiple files per folder
- Generate Markdown documentation
- Export JSON or XML files
- Create nested folder structures
- Skip duplicate folders
- Process multiple worksheets
- Generate project templates

---

## Technologies Used

- Python
- Pandas
- Google Sheets CSV Export

---

## Notes

- The Google Sheet must be shared as **Anyone with the link can view**.
- Invalid filename characters (`< > : " / \ | ? *`) are automatically replaced with `_`.
- The script only reads data from the spreadsheet and does not modify it.

---
