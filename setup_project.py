from pathlib import Path

folders = [
    "src",
    "src/scraper",
    "src/database",
    "src/detector",
    "src/alerts",
    "src/sheets",
    "src/utils",
    "config",
    "data",
    "logs",
    "tests",
    "docs",
]

files = [
    "src/scraper/__init__.py",
    "src/database/__init__.py",
    "src/detector/__init__.py",
    "src/alerts/__init__.py",
    "src/sheets/__init__.py",
    "src/utils/__init__.py",
    ".env",
    ".gitignore",
    "requirements.txt",
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).touch(exist_ok=True)

print("Project structure created successfully!")