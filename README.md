# Code Snippet Organizer

A simple **Python CLI tool** to manage your code snippets efficiently. You can **add, list, search, and export/import** snippets in JSON format.

## Features

- **Add Snippets**: Quickly save your code snippets with title, code, and description.  
- **List Snippets**: View all your saved snippets in a clean format.  
- **Search Snippets**: Find snippets by keywords or tags.  
- **Export/Import**: Export snippets to JSON and import them back for backup or sharing.  

## Folder Structure

project_root/
│
├─ main.py # Entry point for CLI
├─ db.py # Database handling
├─ snippets.py # Core snippet operations
├─ snippets.db # SQLite database (optional)
├─ requirements.txt # Python dependencies
├─ utils/ # Utility modules
│ ├─ display.py
│ ├─ search.py
│ └─ storage.py



> Note: `__pycache__` folders and `venv` are excluded from the repository. Optional temporary files like `snippets.json` and `snippets_export.json` can also be ignored for a clean submission.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/snippet-organizer.git
cd snippet-organizer


python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


pip install -r requirements.txt

python main.py

You will see options:

Add Snippet

List Snippets

Search Snippets

Exit

Export Snippets to JSON

Import Snippets from JSON